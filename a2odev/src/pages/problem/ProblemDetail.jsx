import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { postData } from '../../services/ApiService';

export const ProblemDetail = ( )=>{

  const location = useLocation();

  const problem = location.state.problem;
  const [inputData, setInputData] = useState('');
  const [outputData, setOutputData] = useState('')

  const handleInputChange = (e) => { 
    setInputData(e.target.value)
   }

  const handleSubmit = async (event) => {
    event.preventDefault();
    const data = {
      index: problem.id,
      input: inputData
    }
    try {
      const response = await postData(data);
      if (response) {
        setOutputData(response.data);
      }
    } catch (error) {
      console.log(error);
      setOutputData("error");
    }
  };


    return(
        <div className='app-container'> 
        <nav>
        <Link to="/" className="back-link">Go back</Link>
        </nav>
          <h1>Problem - {problem.title}</h1>
          <div className="sections-container">

          <section className="info-section" >
          <h3>Input format:</h3>
          <ul className="info-list">
            {problem.inputFormat.map((item,index)=>(
            <li key={index}>
              {item}
            </li>))}
          </ul>
          </section>
          <section className="interaction-section wrap-container">
            <div className="wrap-item-div">
            <h3>Input</h3>
            <form className='app-textarea-container' onSubmit={handleSubmit}>
            <label htmlFor={`input-${problem.id}`} className="input-label">Write your input here:</label>
                        <textarea  
                        className="app-textarea"
                        rows={1} 
                        id={`input-${problem.id}`}
                        placeholder="..." 
                        value={inputData} onChange={handleInputChange}>
                        </textarea>
                        
                        <button className='app-button' type="submit">Submit</button>
                    </form>
            </div>
            <div  className="wrap-item-div">
              <h3>Output</h3>
              <span className='output-span'>Output will be displayed here:</span>
              <pre id={`output-${problem.id}`} className="output-pre"> {outputData}</pre>
            </div>
          </section>
        
        </div>
        </div>
    )
}
