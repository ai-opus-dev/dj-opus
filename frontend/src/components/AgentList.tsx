import React, { useEffect, useState } from 'react';

interface Agent {
  id: string;
  name: string;
  role: string;
}

const AgentList: React.FC = () => {
  const [agents, setAgents] = useState<Agent[]>([]);

  useEffect(() => {
    // Simulate fetching agent data from a backend or smart contract
    const fetchAgents = async () => {
      // Replace with actual data fetching logic (e.g., from a contract)
      const data: Agent[] = [
        { id: '1', name: 'Agent 1', role: 'Admin' },
        { id: '2', name: 'Agent 2', role: 'User' },
        { id: '3', name: 'Agent 3', role: 'Moderator' },
      ];
      setAgents(data);
    };
    
    fetchAgents();
  }, []);

  return (
    <div>
      <h2>Agent List</h2>
      <table>
        <thead>
          <tr>
            <th>Agent ID</th>
            <th>Name</th>
            <th>Role</th>
          </tr>
        </thead>
        <tbody>
          {agents.map((agent) => (
            <tr key={agent.id}>
              <td>{agent.id}</td>
              <td>{agent.name}</td>
              <td>{agent.role}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default AgentList;
