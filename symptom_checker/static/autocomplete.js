document.addEventListener('DOMContentLoaded', function () {
    function removeDiacritics(text) {
        return text.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
    }

    let availableKeywords = [
        'durere în gât',
        'febră',
        'tuse',
        'durere în piept',
        'durere în gât',
        'sete excesivă',
        'durere de cap',
        'frisoane',
        'fatigabilitate',
        'oboseală',
        'greață',
        'vărsături',
        'diaree',
        'dureri musculare',
        'dureri articulare',
        'sângerare nazală',
        'dificultăți respiratorii',
        'durere abdominală',
        'sensibilitate la lumină',
        'amorțeală în mâini și picioare',
        'scădere în greutate',
        'urinare frecventă',
        'schimbări în tranzitul intestinal',
        'dificultăți de concentrare',
        'sforăit',
        'pierderea poftei de mâncare',
        'insomnie',
        'palpitații',
        'umflarea membrelor',
        'pierderea auzului',
        'senzație de arsură la urinare',
        'dificultăți de vedere',
        'ochi rosii',
        'tulburări de somn',
        'dureri de spate',
        'nas înfundat',
        'răgușeală',
        'anxietate',
        'pierderea memoriei',
        'apatie',
        'dificultăți în mers',
        'convulsii',
        'modificări ale apetitului',
        'sângerare vaginală',
        'umflături în zona gâtului',
        'modificări ale pigmentării pielii',
        'febră persistentă',
        'tulburări de vorbire',
        'umflături dureroase în articulații',
        'sângerare abdominală',
        'tulburări de coagulare a sângelui'
    ];

    const resultsBox = document.querySelector(".result-box");
    const inputBox = document.getElementById("symptoms");

    inputBox.addEventListener('input', function () {
        let input = removeDiacritics(inputBox.value.toLowerCase().trim());
        let lastWord = input.split(/[\s,]+/).pop();

        // Display suggestions based on the last typed word
        display(getSuggestions(lastWord));
    });

    // Use event delegation for handling clicks on result items
    resultsBox.addEventListener('click', function (event) {
        if (event.target.tagName === 'LI') {
            selectInput(event.target);
        }
    });

    function removeDiacritics(text) {
        return text.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
    }

    function getSuggestions(input) {
        if (input && input.length > 0) {
            return availableKeywords.filter((keyword) => {
                return removeDiacritics(keyword.toLowerCase()).includes(input);
            });
        } else {
            return [];
        }
    }

    function display(result) {
        const content = result.map((list) => {
            return "<li>" + list + "</li>";
        });

        resultsBox.innerHTML = "<ul>" + content.join('') + "</ul>";
    }

    function selectInput(list) {
        let selectedSymptom = list.innerHTML.trim();

        // Get the existing text in the search bar
        let existingText = inputBox.value.trim();

        // Remove the last word from existing text (to replace with selected symptom)
        let newText = existingText.substring(0, existingText.lastIndexOf(" "));

        // Append the selected symptom to the existing text with a comma
        newText += ' ' + selectedSymptom;

        // Set the updated text in the search bar
        inputBox.value = newText;

        // Clear the results box
        resultsBox.innerHTML = '';
    }
});
