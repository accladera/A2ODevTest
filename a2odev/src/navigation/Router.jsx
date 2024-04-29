import { Route, Routes } from "react-router-dom"
import { ProblemDetail } from "../pages/problem/ProblemDetail"
import { problemIds as problemRoutes, routes } from "./RouterConfig"

export const AppRouter = ()=>{
    return(
        <Routes>
        {routes.map((route, index)=>
                <Route key={index} path={route.path} element={route.element}/>
            )}
            {problemRoutes.map((item, index)=>
                <Route key={index} path={`/problem-${item}`} element={<ProblemDetail/>}/>
            ) }
        </Routes>
        
    )
}