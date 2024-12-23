import React from 'react';
import GovernanceDashboard from './GovernanceDashboard';
import AgentList from './AgentList';

const App: React.FC = () => {
  return (
    <div>
      <h1>Governance DApp</h1>
      <GovernanceDashboard />
      <AgentList />
    </div>
  );
};

export default App;
