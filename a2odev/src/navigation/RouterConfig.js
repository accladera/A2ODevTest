import { Home } from "../pages/home/Home";
import { getListExcercises } from "../services/ApiService";


const problemList = getListExcercises();
export const problemIds = problemList.map(item => item.id);
export const routes = [
    {
        path:  '/',
        element: <Home />
    }
]

export const PROBLEM_ROUTE = (problemId) => '/problem-' + problemId;