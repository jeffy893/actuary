import numpy as np
import torch
import torch.nn as nn

from torch.autograd import Variable

import pyro
from pyro.distributions import Normal
from pyro.infer import SVI
from pyro.optim import Adam


class Emitter(nn.Module):
    """
    Parameterizes the bernoulli observation likelihood p(x_t | z_t)
    """
    def __init__(self, input_dim, emission_dim):
        super(Emitter, self).__init__()
        # inititialize the three linear transformations used in the neural network
        self.lin_z_to_hidden = nn.Linear(z_dim, emission_dim)
        self.lin_hidden_to_hidden = nn.Linear(emission_dim, emission_dim)
        self.lin_hidden_to_input = nn.Linear(emission_dim, input_dim)
        # initialize the tow non-linearities used in the neural network
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, z_t):
        """
        Given the latent z at the particular time step t we return the vector
        of prababilities 'ps' that parameterizes the bernoullu distribution
        p(x_t | z_t)
        """
        h1 = self.relu(self.lin_z_to_hidden(z_t))
        h2 = self.relu(self.lin_hidden_to_hidden(h1))
        ps = self.sigmoid(self.lin_hidden_to_input(h2))
        return ps

class GatedTransition(nn.Module):
    """
    Parameterizes the gaussian latent transition probability p(z_t | z_{t-1})
    """
    def __init__(selef, z_dim, transition_dim):
        super(GatedTransition, self).__init__()
        # initializes the six linear transformations used in the neural network
        self.lin_gate_z_to_hidden = nn.Linear(z_dim, transition_dim)
        self.lin_gate_hidden_to_z = nn.Linear(transition_dim, z_dim)
        self.lin_proposed_mean_z_to_hidden = nn.Linear(z_dim, transition_dim)
        self.lin_proposed_mean_hidden_to_z = nn.Linear(transition_dim, z_dim)
        self.lin_sig = nn.Linear(z_dim, z_dim)
        self.lin_z_to_mu = nn.Linear(z_dim, z_dim)
        # modify the default initialization of lin_z_to_mu
        # so that it starts out as the identity function
        self.lin_z_to_mu.weight.data = torch.eye(z_dim)
        self .lin_z_to_mu.bias.data = torch.zeros(z_dim)
        # initialize the three non-linearities used in the neural network
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()
        self.softplus = nn.Softplus()

    def forward(self, z_t_1):
        """
        Given the latent z_{t-1} corresponding to the time step t-1
        we return the mean and tsigma vectors that parameterize the
        (diagonal) gaussian distribution p(z_t | z_{t-1})
        """
        # compute the gating function and one minus the gating function
        gate_intermediate = self.relu(self.lin_gate_z_to_hidden(z_t_1))
        gate = self.sigmoid(self.lin_gate_hidden_to_z(gate_intermediate))
        one_minus_gate = ng_ones(gate.size()).type_as(gate) - gate
        # compute the 'proposed mean'
        proposed_mean_intermediate = self.relu(self.lin_proposed_mean_z_to_hidden(z_t_1))
        proposed_mean = self.lin_proposed_mean_hidden_to_z(proposed_mean_intermediate)
        # assemble the actual mean used to sample z_t, which mixes a linear transformation
        # of z_{t-1} with the proposed mean modulated by the gating function
        mu = one_minus_gate * self.lin_z_to_mu(z_t_1) + gate * proposed_mean
        # compute the sigma used to sample z_t, using the proposed mean from above as input
        # the softplus ensures that sigma is positive
        sigma = self.softplus(self.lin_sig(self.relu(proposed_mean)))
        # return mu, sigma which can be fed into Normal
        return mu, sigma

def model(self, mini_batch, mini_batch_reversed, mini_batch_mask, mini_batch_seq_lengths, annealing_facor=1.0):
    # this is the number of time steps we need to process in the mini-batch
    T_max = mini_batch.size(1)

    # register all pytorch (sub)modules with pyro
    pyro.module("dmm", self)

    # set z_prev = z_0 to setup the recursive conditioning
    z_prev = self.z_0

    # sample the latents z and observed x's one time step at a time
    for t in range(1, T_max + 1):
        # the next three lines of code smaple z_t ~ p(z_t | z_{t-1})
        # first compute the parameters of the diagonal gaussian distribution
        # p(z_t | z_{t-1})
        z_mu, z_sigma = self.trans(z_prev)
        # then sampe z_t according to dist.Normal(z_mu, z_sigma)
        z_t = pyro.sample("z_%d" % t, dist.Normal, z_mu, z_sigma, log_pdf_mask=annealing_factor * mini_batch_mask[:, t-1:t])

        # compute the probabilities that parameterize the bernoulli likelihood
        emission_probs_t = self.emitter(z_t)
        # the next statement instructs pyro to observe x_t according to the
        # bernoulli distribution p(x_t | z_t)
        pyro.observe("obs_x_%d" % t, dist.bernoulli, mini_batch[:, t-1, :], emission_probs_t, log_pdf_mask=mini_batch_mask[:, t-1:t])
        # the latent sampled at this time step will be conditioned upon
        # in the next tiem step so keep track of it
        z_prev = z_t
