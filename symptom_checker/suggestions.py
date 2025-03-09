# suggestions.py
from unidecode import unidecode


def analyze_symptoms(symptoms):
    # Transliteration and conversion of symptoms to lowercase letters
    symptoms = unidecode(symptoms.lower())

    # Dictionary of Symptoms, Associated Conditions, and Descriptions
    symptom_conditions = {
        unidecode('febră'): {
            'conditions': [
                'Răceală : Răceala reprezintă cel mai comun termen pentru infecțiile tractului respirator superior, mai ales nas, gât și sinusuri. Recomandări generale: odihnă și relaxare într-un mediu liniștit,'
                'consumul adecvat de lichide și aplicarea de comprese reci sau calde în funcție de preferințe.',
                'Gripă : Gripa este o afecțiune respiratorie cauzată de virusuri. Este extrem de contagioasă și se răspândește prin tuse, strănut'
                ' sau prin atingerea unei suprafețe infectate. Recomandări generale:  consultația unui medic, odihnă și somn, consumul adecvat de lichide, administrarea de medicamente conform indicațiilor.'],

        },
        unidecode('tuse'): {
            'conditions': [
                'Răceală : Răceala reprezintă cel mai comun termen pentru infecțiile tractului respirator superior, mai ales nas, gât și sinusuri. Recomandări generale: odihnă și relaxare într-un mediu liniștit,'
                'consumul adecvat de lichide și aplicarea de comprese reci sau calde în funcție de preferințe.',
                'Gripă : Gripa este o afecțiune respiratorie cauzată de virusuri. Este extrem de contagioasă și se răspândește prin tuse, strănut'
                ' sau prin atingerea unei suprafețe infectate. Recomandări generale:  consultația unui medic, odihnă și somn, consumul adecvat de lichide, administrarea de medicamente conform indicațiilor.',
                'Bronșită : Bronsita reprezinta inflamatia mucoasei care captuseste bronhiile si bronsiolele si este cauzata de secretia excesiva de mucus. Recomandări generale: consultația unui medic, odihnă, administrarea de medicamente conform indicațiilor.',
                'Infecții respiratorii : O infectie a tractului respirator poate afecta sinusurile, gatul, plamanii sau caile respiratorii. Recomandări generale: consultația unui medic, odihnă, administrarea de medicamente conform indicațiilor'
            ],
        },
        unidecode('durere în gât'): {
            'conditions': [
                'Răceală : Răceala reprezintă cel mai comun termen pentru infecțiile tractului respirator superior, mai ales nas, gât și sinusuri. Recomandări generale: odihnă și relaxare într-un mediu liniștit,'
                'consumul adecvat de lichide și aplicarea de comprese reci sau calde în funcție de preferințe.',
                'Amigdalită : Amigdalita este inflamatia amigdalelor, doua mase de tesut de forma ovala situate in spatele gatului – fiecare amigdala pe cate o parte. Recomandări generale: consultația unui medic, odihnă, gargară cu apă sărată.'
            ],
        },
        unidecode('durere de cap'): {
            'conditions': [
                'Răceală : Răceala reprezintă cel mai comun termen pentru infecțiile tractului respirator superior, mai ales nas, gât și sinusuri. Recomandări generale: odihnă și relaxare într-un mediu liniștit,'
                'consumul adecvat de lichide și aplicarea de comprese reci sau calde în funcție de preferințe.',
                'Gripă : Gripa este o afecțiune respiratorie cauzată de virusuri. Este extrem de contagioasă și se răspândește prin tuse, strănut'
                ' sau prin atingerea unei suprafețe infectate. Recomandări generale:  consultația unui medic, odihnă și somn, consumul adecvat de lichide, administrarea de medicamente conform indicațiilor.',
                'Migrenă : Migrena este in general o durere de cap moderata sau severa resimtita ca o durere pulsatila pe o parte a capului (unilateral). Recomandări generale: odihnă într-un mediu liniștit, aplicarea de comprese reci, medicamente pentru durere.'
            ],
        },
        unidecode('frisoane'): {
            'conditions': [
                'Gripă : Gripa este o afecțiune respiratorie cauzată de virusuri. Este extrem de contagioasă și se răspândește prin tuse, strănut'
                ' sau prin atingerea unei suprafețe infectate. Recomandări generale:  consultația unui medic, odihnă și somn, consumul adecvat de lichide, administrarea de medicamente conform indicațiilor.',
                'Infecție : Invazie a unui organism viu de catre microorganisme patogene care actioneaza prin multiplicarea lor (virulenta) si eventual prin secretarea de toxine. Recomandări generale: odihnă și hidratare, medicamente conforme indicațiilor medicului.'
            ],
        },
        unidecode('fatigabilitate'): {
            'conditions': [
                'Gripă : Gripa este o afecțiune respiratorie cauzată de virusuri. Este extrem de contagioasă și se răspândește prin tuse, strănut'
                ' sau prin atingerea unei suprafețe infectate. Recomandări generale: consultația unui medic, odihnă și somn, consumul adecvat de lichide, administrarea de medicamente conform indicațiilor.',
                'Anemie : Anemia este o afectiune care inseamna deficitul de globule rosii sanatoase. Recomandări generale: Identificarea și tratarea cauzei anemiei, suplimente de fier, consum de alimente bogate în fier.'
            ],
        },
        unidecode('oboseală'): {
            'conditions': [
                'Anemie : Anemia este o afectiune care inseamna deficitul de globule rosii sanatoase. Recomandări generale: Identificarea și tratarea cauzei anemiei, suplimente de fier, consum de alimente bogate în fier.'
            ],
        },
        unidecode('greață'): {
            'conditions': [
                'Gripă : Gripa este o afecțiune respiratorie cauzată de virusuri. Este extrem de contagioasă și se răspândește prin tuse, strănut'
                ' sau prin atingerea unei suprafețe infectate. Recomandări generale: consultația unui medic, odihnă și somn, consumul adecvat de lichide, administrarea de medicamente conform indicațiilor.',
                'Infecție gastro-intestinală : Infecția gastro-intestinală este o afecțiune caracterizată de inflamarea tractului gastro-intestinal, care include stomacul și intestinele. Recomandări generale: Hidratare pentru a preveni deshidratarea, alimentație ușoară, medicamente antidiareice sau antibiotice conform indicațiilor.'
            ],
        },
        unidecode('vărsături'): {
            'conditions': [
                'Gripă : Gripa este o afecțiune respiratorie cauzată de virusuri. Este extrem de contagioasă și se răspândește prin tuse, strănut'
                ' sau prin atingerea unei suprafețe infectate. Recomandări generale: consultația unui medic, odihnă și somn, consumul adecvat de lichide, administrarea de medicamente conform indicațiilor.',
                'Infecție gastro-intestinală : Infecția gastro-intestinală este o afecțiune caracterizată de inflamarea tractului gastro-intestinal, care include stomacul și intestinele. Recomandări generale: Hidratare pentru a preveni deshidratarea, alimentație ușoară, medicamente antidiareice sau antibiotice conform indicațiilor.'
            ],
        },
        unidecode('diaree'): {
            'conditions': [
                'Infecție gastro intestinală : Infecția gastro-intestinală este o afecțiune caracterizată de inflamarea tractului gastro-intestinal, care include stomacul și intestinele. Recomandări generale: Hidratare pentru a preveni deshidratarea, alimentație ușoară, medicamente antidiareice sau antibiotice conform indicațiilor.'
            ],
        },
        unidecode('dureri musculare'): {
            'conditions': [
                'Gripă : Gripa este o afecțiune respiratorie cauzată de virusuri. Este extrem de contagioasă și se răspândește prin tuse, strănut'
                ' sau prin atingerea unei suprafețe infectate. Recomandări generale: consultația unui medic, odihnă și somn, consumul adecvat de lichide, administrarea de medicamente conform indicațiilor.',
                'Febră musculară : Febră musculară este o afecțiune caracterizată prin durere și disconfort la nivelul mușchilor. Este adesea asociată cu efort fizic intens sau cu activități la care mușchii nu sunt obișnuiți. Recomandări generale: Odihnă, aplicarea de comprese reci sau calde, administrarea de analgezice conform indicațiilor.',
                'Întindere musculară : Întinderea musculară, cunoscută și sub denumirea de entorsă musculară, reprezintă o leziune a mușchilor sau tendoanelor. Aceasta rezultă dintr-o forță excesivă sau bruscă aplicată asupra mușchilor/tendoanelor. Recomandări generale: Odihnă, aplicarea de comprese reci sau calde, administrarea de analgezice conform indicațiilor.'
            ],
        },
        unidecode('dureri articulare'): {
            'conditions': [
                'Artrită : Artrita este o afecțiune inflamatorie a articulațiilor care poate afecta una sau mai multe articulații, determinând durere, umflături și rigiditate. Recomandări generale: Odihnă, exerciții fizice ușoare, administrarea de analgezice sau antiinflamatoare conform indicațiilor.',
                'Lupus : Lupusul este o boală autoimună complexă în care sistemul imunitar al organismului atacă propriile celule și țesuturi, provocând inflamație și afectând multiple organe și sisteme. Recomandări generale: Odihnă, protecție solară, administrarea de medicamente imunosupresoare sau antiinflamatoare conform indicațiilor.'
            ],
        },
        unidecode('sângerare nazală'): {
            'conditions': [
                'Rinită alergică : Rinita alergică este o afecțiune inflamatorie a mucoasei nazale, cauzată de reacția sistemului imunitar la substanțe numite alergeni. Recomandări generale: Evitarea alergenilor, utilizarea de umidificatoare, administrarea de antihistaminice conform indicațiilor.',
                'Hipertensiune : Hipertensiunea arterială, cunoscută și sub denumirea de tensiune arterială crescută, este o afecțiune medicală caracterizată prin creșterea presiunii sângelui în artere. Recomandări generale: Adoptarea unui stil de viață sănătos, reducerea consumului de sare, administrarea de medicamente antipresive conform indicațiilor.'
            ],
        },
        unidecode('dificultăți respiratorii'): {
            'conditions': [
                'Astm : Astmul este o afecțiune cronică a căilor respiratorii caracterizată prin inflamația acestora și hipersensibilitatea bronhiilor. Recomandări generale: Evitarea factorilor declanșatori, administrarea de medicamente bronhodilatatoare sau antiinflamatoare conform indicațiilor.',
                'Pneumonie : Pneumonia reprezintă o infecție a parenchimului pulmonar, caracterizată prin inflamația țesuturilor pulmonare. Recomandări generale: Odihnă, administrarea de antibiotice conform indicațiilor, hidratare corespunzătoare.'
            ],
        },
        unidecode('durere abdominală'): {
            'conditions': [
                'Infecție gastro-intestinală : Infecția gastro-intestinală este o afecțiune caracterizată de inflamarea tractului gastro-intestinal, care include stomacul și intestinele. Recomandări generale: Odihnă, hidratare corespunzătoare, administrarea de medicamente antidiareice sau antibiotice conform indicațiilor.',
                'Colită : Colita reprezintă o inflamație a mucoasei intestinului gros (colonului). Recomandări generale: Dieta bogată în fibre, administrarea de medicamente antiinflamatoare sau imunosupresoare conform indicațiilor.'
            ],
        },
        unidecode('sensibilitate la lumină'): {
            'conditions': [
                'Migrenă : Migrena este în general o durere de cap moderată sau severă resimțită ca o durere pulsatilă pe o parte a capului (unilateral). Recomandări generale: Odihnă într-un mediu liniștit, aplicarea de comprese reci, medicamente pentru durere.',
                'Meningită : Meningita reprezintă o inflamație a membranei care acoperă creierul și măduva spinării, cunoscută sub numele de meninge. Recomandări generale: Odihnă într-un mediu întunecat și liniștit, administrarea de medicamente antivirale sau antibiotice conform indicațiilor.'
            ],
        },
        unidecode('amorțeală în mâini și picioare'): {
            'conditions': [
                'Sindromul de tunel carpian : Sindromul de tunel carpian este o afecțiune care apare atunci când nervul median, care rulează de-a lungul brațului în mână, devine comprimat în mâna inferioară. Recomandări generale: Odihnă pentru zona afectată, exerciții de întindere, utilizarea de dispozitive de sprijin pentru mână.',
                'Neuropatie periferică : Neuropatia periferică se referă la o serie de condiții în care nervii periferici care conectează creierul și măduva spinării cu restul corpului sunt afectați. Recomandări generale: Controlul glicemiei (în cazul diabetului), administrarea de medicamente analgezice sau anticonvulsivante conform indicațiilor.'
            ],
        },
        unidecode('scădere în greutate'): {
            'conditions': [
                'Hipertiroidism : Hipertiroidismul este o afecțiune în care glanda tiroidă, o glandă în formă de fluture situată în partea frontală a gâtului, produce prea multe hormoni tiroidieni. Recomandări generale: Evaluare endocrinologică, administrarea de medicamente antitiroidiene sau intervenție chirurgicală.',
                'Diabet : Diabetul este o afecțiune metabolică cronică în care organismul nu poate produce suficientă insulină sau nu poate utiliza eficient insulina pe care o produce. Recomandări generale: Dieta echilibrată, exerciții fizice regulate, monitorizarea glicemiei.'
            ],
        },
        unidecode('urinare frecventă'): {
            'conditions': [
                'Infecție urinară : Infecția urinară este o afecțiune care poate afecta diferite părți ale sistemului urinar, inclusiv vezica, uretra, uretere și rinichi. Recomandări generale: Hidratare corespunzătoare, administrarea de antibiotice conform indicațiilor.'
            ],
        },
        unidecode('sete excesivă'): {
            'conditions': [
                'Diabet : Diabetul este o afecțiune metabolică cronică în care organismul nu poate produce suficientă insulină sau nu poate utiliza eficient insulina pe care o produce. Recomandări generale: Dieta echilibrată, exerciții fizice regulate, monitorizarea glicemiei.'
            ],
        },
        unidecode('schimbări în tranzitul intestinal'): {
            'conditions': [
                'Sindromul intestinului iritabil : Sindromul intestinului iritabil (SII) este o tulburare comună a tractului digestiv care afectează colonul. Recomandări generale: Dieta echilibrată, evitarea alimentelor iritante, gestionarea stresului.',
                'Boala Crohn : Boala Crohn este o afecțiune cronică a tractului gastro-intestinal, caracterizată prin inflamație persistentă și tulburări ale funcționării normale a sistemului digestiv. Recomandări generale: Tratament medicamentos, modificări ale dietei și stilului de viață conform indicațiilor medicului.'
            ],
        },
        unidecode('dificultăți de concentrare'): {
            'conditions': [
                'Stres : Stresul este o reacție naturală a organismului în fața unor situații sau condiții considerate provocatoare sau dificile. Recomandări generale: Gestionarea stresului prin tehnici de relaxare, activități recreative, consiliere psihologică.',
                'Anxietate : Anxietatea este o reacție normală la stres sau la situații tensionate și poate fi o parte naturală a vieții. Recomandări generale: Terapie cognitiv-comportamentală, meditație, exerciții fizice regulate.'
            ],
        },
        unidecode('sforăit'): {
            'conditions': [
                'Apnee de somn : Apneea de somn este o tulburare caracterizată prin întreruperi repetate ale respirației pe durata somnului. Recomandări generale: Adoptarea unei poziții optime de somn, pierderea în greutate, evitarea consumului de alcool și tutun înainte de culcare.',
                'Probleme cu sinusurile : Problemele cu sinusurile se referă la afecțiuni care afectează sinusurile, care sunt cavități umplute cu aer situate în oasele craniului. Recomandări generale: Utilizarea de spray-uri nazale saline, inhalarea vaporilor de apă, administrarea de antihistaminice.'
            ],
        },
        unidecode('pierderea poftei de mâncare'): {
            'conditions': [
                'Depresie : Depresia este o tulburare mentală frecventă caracterizată printr-o stare persistentă de tristețe, lipsă de interes sau plăcere în activități obișnuite și zilnice. Recomandări generale: Terapie psihologică, administrarea de medicamente antidepresive, menținerea unei rutine zilnice regulate.',
                'Boala Crohn : Boala Crohn este o afecțiune cronică a tractului gastro-intestinal. Este caracterizată prin inflamație persistentă și tulburări ale funcționării normale a sistemului digestiv. Recomandări generale: Dieta echilibrată, administrarea de medicamente antiinflamatoare, monitorizarea simptomelor.'
            ],
        },
        unidecode('insomnie'): {
            'conditions': [
                'Stres : Stresul este o reacție naturală a organismului în fața unor situații sau condiții considerate provocatoare sau dificile. Recomandări generale: Adoptarea unui program regulat de somn, crearea unui mediu propice pentru odihnă, evitarea stimulenților înainte de culcare.',
                'Anxietate : Anxietatea este o reacție normală la stres sau la situații tensionate și poate fi o parte naturală a vieții. Recomandări generale: Tehnici de relaxare, meditație, limitarea consumului de cofeină și activități intense înainte de culcare.',
                'Insomnie primară : Insomnia primară este o tulburare de somn caracterizată prin dificultatea persistentă de a adormi sau de a menține somnul. Nu este asociată cu alte condiții medicale sau tulburări de sănătate mentale. Recomandări generale: Terapie cognitiv-comportamentală pentru insomnie (CBT-I), evitarea somniferelor pe termen lung.'
            ],
        },
        unidecode('palpitații'): {
            'conditions': [
                'Fibrilație atrială : Fibrilația atrială este o tulburare cardiacă comună caracterizată de bătăile neregulate ale atrilor, cele două camere superioare ale inimii. Recomandări generale: Medicamente antiaritmice, proceduri de cardioversie, gestionarea factorilor de risc cardiovasculari.',
                'Tahicardie : Tahicardia este o afecțiune caracterizată prin creșterea frecvenței cardiace, în special a ritmului bătăilor inimii, la peste 100 de bătăi pe minut în repaus. Recomandări generale: Evitarea stimulenților, administrarea de medicamente antiaritmice, controlul tensiunii arteriale.'
            ],
        },
        unidecode('umflarea membrelor'): {
            'conditions': [
                'Insuficiență cardiacă : Insuficiența cardiacă reprezintă o afecțiune în care inima nu pompează suficient sânge pentru a satisface cerințele organismului. Recomandări generale: Controlul tensiunii arteriale, administrarea de diuretice, menținerea unei diete sărace în sare.',
                'Boală renală : Boala renală se referă la orice afecțiune care afectează structura sau funcția rinichilor. Aceștia au rol crucial în filtrarea sângelui, eliminarea toxinelor și menținerea echilibrului fluidelor și electroliților în organism. Recomandări generale: Hidratare adecvată, limitarea consumului de sodiu, monitorizarea funcției renale.'
            ],
        },
        unidecode('pierderea auzului'): {
            'conditions': [
                'Infecție la ureche : Infecția la ureche reprezintă o inflamație care poate afecta diferite părți ale urechii, inclusiv urechea externă, medie sau internă. Recomandări generale: Administrarea de antibiotice, evitarea expunerii la apă în ureche.',
                'Pierdere de auz : Pierderea de auz se referă la reducerea sau absența capacității de a auzi sunete. Recomandări generale: Consultarea unui specialist ORL, utilizarea dispozitivelor auditive dacă este necesar, protejarea urechilor împotriva zgomotelor puternice.'
            ],
        },
        unidecode('senzație de arsură la urinare'): {
            'conditions': [
                'Infecție urinară : Infecția urinară este o afecțiune care poate afecta diferite părți ale sistemului urinar, inclusiv vezica, uretra, ureterele sau rinichii. Recomandări generale: Hidratare corespunzătoare, administrarea de antibiotice conform indicațiilor.',
                'Infecție cu transmitere sexuală : Infecția cu transmitere sexuală este o afecțiune cauzată de transmiterea bacteriilor, virușilor sau altor microorganisme de la o persoană la alta prin contact sexual. Recomandări generale: Utilizarea prezervativelor, testarea regulată pentru infecțiile cu transmitere sexuală, comunicarea deschisă cu partenerul sexual și profesionistul medical.'
            ],
        },

        unidecode('dificultăți de vedere'): {
            'conditions': [
                'Glaucom : Glaucomul este o afecțiune oculară progresivă care afectează nervul optic și poate duce la pierderea vederii. Recomandări generale: Controlul regulat al presiunii intraoculare, utilizarea medicamentelor prescrise, evitarea expunerii excesive la lumină puternică.',
                'Degenerescență maculară : Degenerescența maculară este o afecțiune oculară legată de vârstă care afectează macula, partea centrală a retinei, responsabilă pentru vederea clară și detaliată. Recomandări generale: Supravegherea atentă a simptomelor, adoptarea unui stil de viață sănătos, includerea nutrienților benefici pentru ochi în dietă.'
            ],
        },

        unidecode('ochi rosii'): {
            'conditions': [
                'Conjunctivită : Conjunctivita, cunoscută și sub denumirea de ochi roșii, este o inflamație a membranei transparente care acoperă partea albă a ochiului și interiorul pleoapelor. Poate fi cauzată de infecții virale sau bacteriene, alergii sau iritații. Recomandări generale: Spălarea ochilor cu apă curată, utilizarea picăturilor oftalmice, evitarea atingerii ochilor cu mâinile murdare.',
                'Oboseală oculară : Oboseala oculară poate duce la roșeața ochilor, în special după perioade prelungite de citit, utilizarea dispozitivelor electronice sau expunerea la lumină puternică. Recomandări generale: Pauze regulate, exerciții oculare, folosirea corectă a ochelarilor de protecție.'
            ],
        },
        unidecode('tulburări de somn'): {
            'conditions': [
                'Somnambulism : Somnambulismul, cunoscut și sub denumirea de mers în somn, este un tulburare de somn în care o persoană se ridică și se deplasează în timpul somnului, având aparența de a fi trează. Recomandări generale: Asigurarea unui mediu sigur în jurul patului, evitarea oboselii excesive, program regulat de somn.',
                'Parasomnii : Parasomniile reprezintă o categorie de tulburări de somn caracterizate prin comportamente anormale, emoții sau evenimente care apar în timpul somnului. Recomandări generale: Crearea unui mediu de somn confortabil, gestionarea stresului, evitarea consumului de alcool și cafeină înainte de culcare.'
            ],
        },
        unidecode('dureri de spate'): {
            'conditions': [
                'Hernie de disc : Hernia de disc reprezintă o afecțiune a coloanei vertebrale în care partea interioară a unui disc intervertebral iese din forma sa normală. Asupra nervilor din apropiere se exercită presiune, cauzând durere și disconfort. Recomandări generale: Exerciții de întărire a spatelui, terapie fizică, gestionarea corectă a greutății corporale.',
                'Spasme musculare : Spasmele musculare reprezintă contracții involuntare și dureroase ale unui mușchi sau grup de mușchi. Aceste contracții pot apărea brusc și pot varia în intensitate de la ușoară la severă. Recomandări generale: Odihnă și aplicarea de gheață/ căldură, masaj, exerciții de întindere a mușchilor.'
            ],
        },

        unidecode('nas înfundat'): {
            'conditions': [
                'Rinită alergică : Rinita alergică este o afecțiune inflamatorie a mucoasei nazale, cauzată de reacția sistemului imunitar la alergeni precum polenul, acarienii sau blana animalelor. Recomandări generale: Evitarea alergenilor, antihistaminice, picături nazale.',
                'Sinuzită : Sinuzita reprezintă inflamația sinusurilor, care sunt cavități umplute cu aer în oasele craniului. Poate fi acută sau cronică și este adesea cauzată de infecții bacteriene sau virale. Recomandări generale: Antibiotice (dacă e cazul), decongestionante, hidratare.',
                'Polipi nazali : Polipii nazali sunt creșteri moi, necanceroase, ce pot obstrucționa pasajele nazale și determina nas înfundat. Recomandări generale: Tratament medicamentos sau chirurgical, în funcție de mărime și simptome.',
            ],
        },

        unidecode('răgușeală'): {
            'conditions': [
                'Laringită : Laringita este inflamația laringelui, care poate cauza răgușeală și dificultăți în vorbire. Poate fi cauzată de infecții virale sau bacteriene, expunerea la iritanți sau suprasolicitare vocală. Recomandări generale: Odihnă vocală, hidratare, evitarea factorilor iritanți.',
                'Reflux gastroesofagian : Refluxul gastroesofagian este o condiție în care acidul din stomac se întoarce în esofag, cauzând iritație și răgușeală. Recomandări generale: Evitarea alimentelor iritante, ridicarea capului în timpul somnului, medicamente antiacide.',
            ],
        },

        unidecode('anxietate'): {
            'conditions': [
                'Anxietate generalizată : Anxietatea generalizată este o tulburare de anxietate caracterizată prin neliniște excesivă în legătură cu diverse aspecte ale vieții, fără un motiv clar sau specific. Recomandări generale: Terapie cognitiv-comportamentală, meditație, administrarea de medicamente anxiolitice sub supravegherea unui specialist.',
                'Atac de panică : Un atac de panică este o manifestare bruscă și intensă de frică sau anxietate care atinge un punct critic în câteva minute. Recomandări generale: Respirație controlată, tehnici de relaxare, terapie de expunere graduală la situații anxiogene.'
            ],
        },
        unidecode('pierderea memoriei'): {
            'conditions': [
                'Alzheimer : Alzheimerul este o boală progresivă a creierului care afectează memorie, gândirea și comportamentul. Recomandări generale: Gestionarea simptomelor, susținerea emoțională și fizică, implicarea în activități cognitive.',
                'Demență vasculară : Demența vasculară este un tip de demență cauzat de deteriorarea vaselor de sânge care furnizează oxigen și nutrienți creierului. Recomandări generale: Controlul factorilor de risc vasculari, inclusiv tensiunea arterială și colesterolul, adoptarea unui stil de viață sănătos.'
            ],
        },
        unidecode('apatie'): {
            'conditions': [
                'Demență vasculară : Demența vasculară este un tip de demență cauzat de deteriorarea vaselor de sânge care furnizează oxigen și nutrienți creierului. Recomandări generale: Managementul simptomelor, încurajarea participării în activități sociale, suport emoțional pentru pacient și familie.',
                'Depresie : Depresia este o tulburare mentală frecventă caracterizată printr-o stare persistentă de tristețe, lipsă de interes sau plăcere în activități obișnuite. Acestea împreună cu o serie de alte simptome afectează modul în care o persoană se simte, gândește și gestionează activitățile zilnice. Recomandări generale: Consiliere psihologică, administrarea de medicamente antidepresive, sprijin social.'
            ],
        },
        unidecode('dificultăți în mers'): {
            'conditions': [
                'Demență vasculară : Demența vasculară este un tip de demență cauzat de deteriorarea vaselor de sânge care furnizează oxigen și nutrienți creierului. Recomandări generale: Managementul simptomelor, sprijin emoțional pentru pacient și familie, activități fizice ușoare.',
                'Neuropatie periferică : Neuropatia periferică se referă la o serie de condiții în care nervii periferici care conectează creierul și măduva spinării cu restul corpului sunt afectați. Recomandări generale: Tratarea cauzei subiacente, medicamente pentru controlul durerii, terapie fizică.'
            ],
        },
        unidecode('convulsii'): {
            'conditions': [
                'Epilepsie : Epilepsia este o afecțiune neurologică cronică care afectează activitatea electrică a creierului, provocând episoade recurente de convulsii sau crize. Recomandări generale: Administrarea de medicamente antiepileptice, evitarea factorilor declanșatori, monitorizarea atentă.',
                'Convulsii febrile : Convulsiile febrile sunt episoade de convulsii care apar în copilărie, de obicei între vârsta de 6 luni și 5 ani, și sunt asociate cu febra înaltă. Recomandări generale: Controlul febrei cu medicamente antitermice, consultarea medicului în caz de convulsii recurente.'
            ],
        },
        unidecode('modificări ale apetitului'): {
            'conditions': [
                'Anorexie : Anorexia nervoasă este un tulburare de alimentație caracterizată printr-o preocupare excesivă față de greutatea și formă corporală, determinând o restricție severă a consumului alimentar și, în consecință, o scădere semnificativă în greutate. Recomandări generale: Terapie nutrițională, consiliere psihologică, sprijin familial.',
                'Bulimie : Bulimia nervoasă este o tulburare de alimentație caracterizată prin episoade recurente de alimentație excesivă (episoade de hiperfagie) urmate de comportamente compensatorii. Aceste comportamente pot fi vărsăturile autoinduse, utilizarea excesivă a laxativelor sau exerciții fizice intense. Recomandări generale: Terapie cognitiv-comportamentală, consiliere nutritională, suport emoțional.'
            ],
        },
        unidecode('sângerare vaginală'): {
            'conditions': [
                'Endometrioză : Endometrioza este o afecțiune medicală în care țesutul similar endometrului, care ar trebui să acopere interiorul uterului, crește în afara acestuia. Recomandări generale: Administrarea de medicamente pentru controlul simptomelor, intervenții chirurgicale în anumite cazuri, gestionarea durerii.',
                'Cancer cervical : Cancerul cervical este o afecțiune malignă care începe în celulele colului uterin, partea inferioară a uterului care se conectează cu vaginul. Recomandări generale: Teste de screening regulate, vaccinare împotriva HPV, tratament personalizat în funcție de stadiul cancerului.'
            ],
        },

        unidecode('umflături în zona gâtului'): {
            'conditions': [
                'Lipom : Un lipom este o formațiune de țesut moale, benignă, care apare sub piele. Este o tumoare grasă non-canceroasă, alcătuită în principal din celule grase. Recomandări generale: Monitorizarea lipomului, intervenție chirurgicală în cazuri selecționate, evaluare periodică.',
                'Limfom : Limfomul reprezintă un tip de cancer care afectează sistemul limfatic, o parte importantă a sistemului imunitar al organismului. Recomandări generale: Tratament individualizat (chimioterapie, radioterapie, terapie țintită), monitorizare atentă a simptomelor, sprijin emoțional.'
            ],
        },
        unidecode('modificări ale pigmentării pielii'): {
            'conditions': [
                'Melanom : Melanomul este o formă de cancer de piele care se dezvoltă în celulele pigmentare numite melanocite. Aceste celule produc melanina, pigmenții responsabili pentru culoarea pielii. Recomandări generale: Examinare dermatologică regulată, protecție solară adecvată, îndepărtarea chirurgicală a melanomului.',
                'Vitiligo : Vitiligo este o afecțiune a pielii caracterizată prin pierderea treptată a pigmentului, cunoscut sub denumirea de melanină, care conferă culoare pielii. Recomandări generale: Terapii de repigmentare, protecție solară, sprijin psihologic.'
            ],
        },
        unidecode('febră persistentă'): {
            'conditions': [
                'Tuberculoză : Tuberculoza este o boală infecțioasă cauzată de bacteria Mycobacterium tuberculosis. Această afecțiune poate afecta mai multe organe ale corpului, în special plămânii, și se transmite prin inhalarea picăturilor de salivă sau secreții respiratorii ale unei persoane infectate. Recomandări generale: Tratament antibiotic specific, monitorizare atentă, evitarea răspândirii la alte persoane.',
                'HIV : Infecția cu virusul imunodeficienței umane (HIV) este o afecțiune virală care afectează sistemul imunitar al organismului, slăbindu-l și făcându-l mai susceptibil la alte infecții și boli. Recomandări generale: Terapie antiretrovirală, monitorizare medicală continuă, gestionarea co-morbidităților.'
            ],
        },
        unidecode('durere în piept'): {
            'conditions': [
                'Angină : Angina, cunoscută și sub denumirea de angină pectorală, este o afecțiune caracterizată prin durere sau disconfort în zona pieptului. Această senzație neplăcută apare atunci când mușchii inimii nu primesc suficient sânge oxigenat. Recomandări generale: Medicamente antianginoase, modificări ale stilului de viață, monitorizare cardiacă regulată.',
                'Infarct miocardic : Infarctul miocardic mai este cunoscut și sub denumirea de atac de cord. Este o afecțiune medicală gravă care apare atunci când fluxul de sânge către o parte a mușchiului inimii este blocat, ducând la moartea celulelor musculare cardiace. Recomandări generale: Urgență medicală, terapie de reperfuzie, tratament post-infecție.'
            ],
        },
        unidecode('tulburări de vorbire'): {
            'conditions': [
                'Accident vascular cerebral : Accidentul vascular cerebral (AVC) mai este cunoscut și sub denumirea de atac cerebral. Este o afecțiune medicală gravă care apare atunci când alimentarea cu sânge a unei părți a creierului este întreruptă sau redusă semnificativ. Recomandări generale: Urgență medicală, recuperare post-AVC, terapie de vorbire și limbaj.',
                'Boală neurodegenerativă : Boala neurodegenerativă este o categorie largă de afecțiuni caracterizate prin deteriorarea progresivă a structurilor și funcțiilor sistemului nervos. Recomandări generale: Gestionarea simptomelor, sprijin emoțional și psihologic, tratamente simptomatice.'
            ],
        },
        unidecode('umflături dureroase în articulații'): {
            'conditions': [
                'Artrită reumatoidă : Artrita reumatoidă este o boală autoimună cronică care afectează articulațiile, determinând inflamație, durere, umflături și, în timp, deteriorarea țesutului articular. Recomandări generale: Medicamente antiinflamatoare, terapie fizică, gestionarea stresului.',
                'Guta : Guta este o formă de artrită inflamatorie care apare ca rezultat al acumulării excesive de acid uric în organism. Recomandări generale: Medicamente pentru controlul acidului uric, modificări ale dietei, hidratare adecvată.'
            ],
        },
        unidecode('sângerare abdominală'): {
            'conditions': [
                'Ulcer : Ulcerul se referă la o leziune sau eroziune în mucoasa stomacului sau a altor părți ale tractului gastrointestinal. Recomandări generale: Medicamente antiacide, antibiotice (dacă ulcerul este cauzat de bacteriile Helicobacter pylori), evitarea factorilor iritanți.',
                'Cancer gastro-intestinal : Cancerul gastro-intestinal se referă la dezvoltarea anormală și necontrolată a celulelor maligne în tractul digestiv. Recomandări generale: Tratament individualizat (chirurgie, chimioterapie, radioterapie), gestionarea simptomelor, suport medical și psihologic.'
            ],
        },
        unidecode('tulburări de coagulare a sângelui'): {
            'conditions': [
                'Hemofilie : Hemofilia este o afecțiune ereditară rară și cronică, caracterizată prin incapacitatea organismului de a produce suficiente proteine de coagulare a sângelui, cunoscute sub denumirea de factori de coagulare. Recomandări generale: Managementul sângerărilor, terapie de substituție a factorilor de coagulare, monitorizare medicală constantă.',
                'Leucemie : Leucemia reprezintă un tip de cancer care afectează celulele sanguine, în special cele responsabile pentru producerea sângelui în măduva osoasă. Recomandări generale: Tratament specific (chimioterapie, transplant de măduvă osoasă), gestionarea efectelor secundare, susținere medicală și emoțională.'
            ],
        },
    }

    suggestions_set = set()

    # Go through the symptoms and look for associated conditions in the dictionary
    for symptom, data in symptom_conditions.items():
        if symptom in symptoms:
            for condition in data['conditions']:
                # Split the condition at the first occurrence of '-'
                parts = condition.split(':', 1)

                # Check if the split succeeded
                if len(parts) == 2:
                    # Get the words before '-' and after '-'
                    first_part = parts[0].strip()
                    second_part = parts[1].strip()

                    # Format the HTML with a span around the words before '-'
                    # styled_sentence = f'<span class="styled-first-part">{first_part}</span> : <br>{second_part}'
                    styled_sentence = f'<span class="styled-first-part">{first_part}</span> : <br>{second_part.replace("Recomandări generale", "<strong>Recomandări generale</strong>")}'
                    suggestions_set.add(styled_sentence)
                    # Adaugă un rând liber între fiecare afecțiune și descriere
                    suggestions_set.add('')

    # suggestions_set = list(suggestions_set)  # Convert set to list if needed
    if not suggestions_set:
        return {'Nu s-au găsit afecțiuni. Consultați un medic pentru evaluare.'}

    suggestions_list = list(suggestions_set)

    # Replace '.' with '.<br>' to add a line break after each period
    suggestions_list = [s.replace('.', '.<br>') for s in suggestions_list]
    suggestions_list = [s.replace('!', '<br>*') for s in suggestions_list]

    # Return the modified list
    return suggestions_list
