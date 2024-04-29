import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { PROBLEM_ROUTE } from '../../navigation/RouterConfig';
import { getListExcercises as getProblems } from '../../services/ApiService';

export const Home =()=>{
    const navigate= useNavigate();

    const [problems, setProblems] = useState([]);

    useEffect(() => {
        loadProblems();
    }, []);

const loadProblems = ()=>{
        setProblems(getProblems());
}

const openProblem = (item)=>{
    navigate(PROBLEM_ROUTE(item.id),
    {
        state:{
            problem: item
        }
    });
}

    return(
        <div className="app-container">
        <h1>Technical Test</h1>
        <small>Choose the problem: </small>
        <div className="button-list box-border">
                {
                problems.map((item, index)=>(
                    <div key={index} className='wrap-item-button' >
                    <button   className="app-button" onClick={()=>openProblem(item)}>{item.title}</button>            
                    </div>
                ))
            }
        </div>
        </div>
    );
}
