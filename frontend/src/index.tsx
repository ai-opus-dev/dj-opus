import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import AgentsPage from './pages/agents';
import GovernancePage from './pages/GovernancePage';
import MarketplacePage from './pages/MarketplacePage';

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/agents" element={<AgentsPage />} />
        <Route path="/governance" element={<GovernancePage />} />
        <Route path="/marketplace" element={<MarketplacePage />} />
      </Routes>
    </Router>
  );
};

export default App;
