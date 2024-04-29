import { BrowserRouter } from 'react-router-dom';
import './styles/App.css';
import { AppRouter } from './navigation/Router';
import { NavHeader } from './components/Nav';


function App() {
  return (
    <div className="App">
      <NavHeader />
      <BrowserRouter> 
        <AppRouter></AppRouter>
      </BrowserRouter>
    </div>
  );
}

export default App;
