from sympy import *

x = symbols('x')
n = symbols('n')


l = 3

f = (-6.03203917069319E-122*(0.35714*(x - 1))**86 + 4.4045447769375995E-119*(0.35714*(x - 1))**85 + -1.36550331178403E-116*(0.35714*(x - 1))**84 + 2.3153190607096934E-114*(0.35714*(x - 1))**83 + -2.3453840258054397E-112*(0.35714*(x - 1))**82 + 1.599792636438187E-110*(0.35714*(x - 1))**81 + -1.030185983067853E-108*(0.35714*(x - 1))**80 + 6.26709302846239E-107*(0.35714*(x - 1))**79 + -2.356130303840225E-106*(0.35714*(x - 1))**78 + -2.0969184761526165E-103*(0.35714*(x - 1))**77 + -1.0597793593155685E-101*(0.35714*(x - 1))**76 + 1.7311901360377767E-99*(0.35714*(x - 1))**75 + 8.481999813568444E-98*(0.35714*(x - 1))**74 + -5.954261552365314E-96*(0.35714*(x - 1))**73 + -1.3741163004811682E-93*(0.35714*(x - 1))**72 + 1.0597691026614895E-91*(0.35714*(x - 1))**71 + 1.6626573734873231E-90*(0.35714*(x - 1))**70 + -3.250949750856738E-88*(0.35714*(x - 1))**69 + 1.4334021273414475E-86*(0.35714*(x - 1))**68 + -1.1907812077334204E-84*(0.35714*(x - 1))**67 + 1.4802515010439455E-83*(0.35714*(x - 1))**66 + 5.459158090287821E-81*(0.35714*(x - 1))**65 + -1.630587505778277E-79*(0.35714*(x - 1))**64 + -1.4803168438229959E-78*(0.35714*(x - 1))**63 + -9.164815694980572E-78*(0.35714*(x - 1))**62 + -1.2965899296278589E-73*(0.35714*(x - 1))**61 + 1.0461562018075577E-71*(0.35714*(x - 1))**60 + 4.3529379693059174E-70*(0.35714*(x - 1))**59 + -6.56895681818942E-68*(0.35714*(x - 1))**58 + 1.1621400960611923E-66*(0.35714*(x - 1))**57 + 6.9403606336315626E-65*(0.35714*(x - 1))**56 + -3.3732254398071835E-63*(0.35714*(x - 1))**55 + 3.1598550421161966E-61*(0.35714*(x - 1))**54 + -2.3961568284164244E-59*(0.35714*(x - 1))**53 + 3.562500015947179E-58*(0.35714*(x - 1))**52 + 1.678408327963288E-56*(0.35714*(x - 1))**51 + 4.655721382340218E-55*(0.35714*(x - 1))**50 + -3.616520481798224E-53*(0.35714*(x - 1))**49 + -1.8652069277922125E-51*(0.35714*(x - 1))**48 + 1.1189119708532935E-49*(0.35714*(x - 1))**47 + -9.116466945239888E-48*(0.35714*(x - 1))**46 + 1.129074534097147E-45*(0.35714*(x - 1))**45 + -5.237259917505068E-44*(0.35714*(x - 1))**44 + 3.5007208621753732E-43*(0.35714*(x - 1))**43 + 1.3069209390350787E-41*(0.35714*(x - 1))**42 + 2.3561726586345317E-39*(0.35714*(x - 1))**41 + -1.2067594268347845E-37*(0.35714*(x - 1))**40 + -1.682452346093721E-36*(0.35714*(x - 1))**39 + 2.064066752906555E-34*(0.35714*(x - 1))**38 + -6.06747925996285E-34*(0.35714*(x - 1))**37 + -2.7651751527442602E-31*(0.35714*(x - 1))**36 + 9.238507558923289E-30*(0.35714*(x - 1))**35 + -1.9886471128157801E-28*(0.35714*(x - 1))**34 + 8.990772032638234E-27*(0.35714*(x - 1))**33 + -2.1798603155996638E-25*(0.35714*(x - 1))**32 + -1.356452942100118E-23*(0.35714*(x - 1))**31 + 1.2937815760189185E-21*(0.35714*(x - 1))**30 + -4.916035139758396E-20*(0.35714*(x - 1))**29 + 9.355155751618688E-19*(0.35714*(x - 1))**28 + 1.7825110853096693E-18*(0.35714*(x - 1))**27 + -7.242319021082832E-16*(0.35714*(x - 1))**26 + 2.3800939509664258E-14*(0.35714*(x - 1))**25 + -3.2454753463669927E-13*(0.35714*(x - 1))**24 + -4.209580257196908E-12*(0.35714*(x - 1))**23 + 3.17102755395527E-10*(0.35714*(x - 1))**22 + -7.218109394221449E-9*(0.35714*(x - 1))**21 + 5.281353279967509E-8*(0.35714*(x - 1))**20 + 1.8505687396249133E-6*(0.35714*(x - 1))**19 + -7.998196775150962E-5*(0.35714*(x - 1))**18 + 0.0017825720626199581*(0.35714*(x - 1))**17 + -0.028992786777197528*(0.35714*(x - 1))**16 + 0.3866325029038041*(0.35714*(x - 1))**15 + -4.5596311340375175*(0.35714*(x - 1))**14 + 49.6630907374238*(0.35714*(x - 1))**13 + -498.24889786484874*(0.35714*(x - 1))**12 + 4437.243565030405*(0.35714*(x - 1))**11 + -33618.27839154101*(0.35714*(x - 1))**10 + 209663.7350026045*(0.35714*(x - 1))**9 + -1050794.9124027481*(0.35714*(x - 1))**8 + 4145493.597961421*(0.35714*(x - 1))**7 + -1.258508079788846E7*(0.35714*(x - 1))**6 + 2.8542952084078625E7*(0.35714*(x - 1))**5 + -4.63262556940537E7*(0.35714*(x - 1))**4 + 5.0246265947098136E7*(0.35714*(x - 1))**3 + -3.215313410168407E7*(0.35714*(x - 1))**2 + 9000802.962808762*(0.35714*(x - 1))**1)/193.961


f = f/6596.55660183798

fi = integrate(f,(x,1,4))

a_0 = (1/2*l)*fi

fa = f*cos( (n*pi*x)/l )

a_n = (1/l)*integrate(fa,(x,1,4))

pprint(simplify(a_n))

fb = f*sin( (n*pi*x)/l )

b_n = (1/l)*integrate(fb,(x,1,4))

pprint(simplify(b_n))


#eq = a0 + Sum(a_n*cos((n*pi*x)/l)) + Sum(b_n*sin((n*pi*x)/l))

#pprint(simplify(eq))
