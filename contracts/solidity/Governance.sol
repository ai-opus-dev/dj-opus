// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract Governance {
    IERC20 public token;
    address public owner;

    uint256 public proposalCount;
    uint256 public votingDuration; // in seconds

    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 endTime;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        mapping(address => bool) voted;
    }

    mapping(uint256 => Proposal) public proposals;

    event ProposalCreated(uint256 id, address proposer, string description, uint256 endTime);
    event Voted(uint256 proposalId, address voter, bool support, uint256 weight);
    event ProposalExecuted(uint256 proposalId, bool success);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    constructor(IERC20 _token, uint256 _votingDuration) {
        token = _token;
        owner = msg.sender;
        votingDuration = _votingDuration;
    }

    function createProposal(string memory _description) external {
        proposalCount++;
        Proposal storage proposal = proposals[proposalCount];
        proposal.id = proposalCount;
        proposal.proposer = msg.sender;
        proposal.description = _description;
        proposal.endTime = block.timestamp + votingDuration;

        emit ProposalCreated(proposal.id, msg.sender, _description, proposal.endTime);
    }

    function vote(uint256 _proposalId, bool _support) external {
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp < proposal.endTime, "Voting has ended");
        require(!proposal.voted[msg.sender], "Already voted");

        uint256 votingPower = token.balanceOf(msg.sender);
        require(votingPower > 0, "No voting power");

        proposal.voted[msg.sender] = true;
        if (_support) {
            proposal.forVotes += votingPower;
        } else {
            proposal.againstVotes += votingPower;
        }

        emit Voted(_proposalId, msg.sender, _support, votingPower);
    }

    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp >= proposal.endTime, "Voting is still ongoing");
        require(!proposal.executed, "Proposal already executed");

        proposal.executed = true;

        bool success = proposal.forVotes > proposal.againstVotes;
        emit ProposalExecuted(_proposalId, success);
    }

    function setVotingDuration(uint256 _newDuration) external onlyOwner {
        votingDuration = _newDuration;
    }
}
