let question_number = 0
let correct_answers = 0

let question_number_text = document.querySelector("#question-number")
let question_title = document.querySelector("#question-title")
let question_text = document.querySelector("#question-body")

let question_input = document.querySelector("#question-input")
let submit_button = document.querySelector("#submit")

const intro_text = "Welcome to the quiz!"


const init = () => {

    question_title.innerHTML = intro_text
    question_text.innerHTML = "Click the button below to start the quiz"

}

submit_button.addEventListener("click", () => {
    handle_submit()
})

question_input.addEventListener("keypress", (e) => {
    if (e.key == "Enter") {
        handle_submit()
    }
})



const handle_submit = () => {
    if (question_number == 0) {
        show_question_input()
    }

    if (question_number != 0) {
        mark_question()
    }

    if (question_number == questions.length) {
        finish_quiz()
        return
    }


    question_to_add = questions[question_number]

    question_title.innerHTML = question_to_add.title
    question_text.innerHTML = question_to_add.text
    question_number_text.innerHTML = `Question ${question_number + 1} of ${questions.length}`

    MathJax.typeset()
    question_number++

}

const MD5 = (string) => {
    return CryptoJS.MD5(string).toString()
}

const show_question_input = () => {
    question_input.style.display = "block"
}

const mark_question = () => {
    let question_to_mark = questions[question_number - 1]
    let answer = question_input.value
    if (MD5(answer) == question_to_mark.solution_hash) {
        correct_answers++
    }
    question_input.value = ""
}

const finish_quiz = () => {

    question_title.innerHTML = "Quiz finished!"
    question_text.innerHTML = `You got ${correct_answers} out of ${questions.length} questions correct!`
    question_number_text.innerHTML = ""
    question_input.style.display = "none"
    submit_button.style.display = "none"
}

init()