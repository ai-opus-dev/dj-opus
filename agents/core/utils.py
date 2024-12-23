from reward_system import RewardSystem

# Initialize the reward system
reward_system = RewardSystem()

# Add rewards
print(reward_system.add_reward("user1", 100))

# Check balance
print(reward_system.get_reward_balance("user1"))

# Redeem rewards
print(reward_system.redeem_rewards("user1", 50))

# Transfer rewards
print(reward_system.add_reward("user2", 50))
print(reward_system.transfer_rewards("user1", "user2", 30))

# Print system state
print(reward_system)
