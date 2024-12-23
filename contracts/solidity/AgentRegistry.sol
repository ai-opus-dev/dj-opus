// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AgentRegistry {
    address public owner;
    uint256 public agentCount;

    struct Agent {
        uint256 id;
        address addr;
        string name;
        string details;
        bool isActive;
    }

    mapping(uint256 => Agent) public agents;
    mapping(address => uint256) public agentIds;

    event AgentRegistered(uint256 id, address addr, string name, string details);
    event AgentUpdated(uint256 id, address addr, string name, string details);
    event AgentStatusUpdated(uint256 id, address addr, bool isActive);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    modifier onlyAgent(uint256 _id) {
        require(agents[_id].addr == msg.sender, "Not the agent");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function registerAgent(string memory _name, string memory _details) external {
        require(agentIds[msg.sender] == 0, "Agent already registered");

        agentCount++;
        agents[agentCount] = Agent({
            id: agentCount,
            addr: msg.sender,
            name: _name,
            details: _details,
            isActive: true
        });

        agentIds[msg.sender] = agentCount;

        emit AgentRegistered(agentCount, msg.sender, _name, _details);
    }

    function updateAgentDetails(uint256 _id, string memory _name, string memory _details) external onlyAgent(_id) {
        Agent storage agent = agents[_id];
        agent.name = _name;
        agent.details = _details;

        emit AgentUpdated(_id, agent.addr, _name, _details);
    }

    function updateAgentStatus(uint256 _id, bool _isActive) external onlyOwner {
        Agent storage agent = agents[_id];
        agent.isActive = _isActive;

        emit AgentStatusUpdated(_id, agent.addr, _isActive);
    }

    function getAgent(uint256 _id) external view returns (Agent memory) {
        return agents[_id];
    }

    function getAgentByAddress(address _addr) external view returns (Agent memory) {
        uint256 id = agentIds[_addr];
        require(id != 0, "Agent not found");
        return agents[id];
    }
}
