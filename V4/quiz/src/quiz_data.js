//Quiz Data
import { getQuestions, CategoryNames } from "open-trivia-db";

const questiondifficulties = document.getElementById("questiondifficulties");
const questionamount = document.getElementById("questionamount");
const questioncategory = document.getElementById("questioncategory");

const questions = await getQuestions({
  amount: QuestionAmount.questionamount,
  category: CategoryNames.questioncategory,
  difficulty: QuestionDifficulties.questiondifficulties,
})