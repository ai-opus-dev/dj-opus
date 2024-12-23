class RewardSystem:
    def __init__(self, initial_rewards=None):
        """
        Initialize the RewardSystem with an optional dictionary of rewards.

        :param initial_rewards: A dictionary where keys are user IDs and values are reward balances.
        """
        self.rewards = initial_rewards or {}

    def add_reward(self, user_id, amount):
        """
        Add rewards to a user's account.

        :param user_id: The ID of the user.
        :param amount: The amount to add.
        """
        if amount < 0:
            raise ValueError("Reward amount cannot be negative.")
        
        if user_id not in self.rewards:
            self.rewards[user_id] = 0
        
        self.rewards[user_id] += amount
        return f"Added {amount} rewards to user {user_id}. New balance: {self.rewards[user_id]}."

    def get_reward_balance(self, user_id):
        """
        Get the reward balance of a user.

        :param user_id: The ID of the user.
        :return: The user's reward balance.
        """
        return self.rewards.get(user_id, 0)

    def redeem_rewards(self, user_id, amount):
        """
        Redeem rewards for a user.

        :param user_id: The ID of the user.
        :param amount: The amount to redeem.
        :return: A message confirming the redemption.
        """
        if user_id not in self.rewards:
            raise ValueError(f"User {user_id} has no rewards.")
        
        if self.rewards[user_id] < amount:
            raise ValueError(f"User {user_id} has insufficient rewards.")
        
        self.rewards[user_id] -= amount
        return f"Redeemed {amount} rewards for user {user_id}. Remaining balance: {self.rewards[user_id]}."

    def transfer_rewards(self, from_user, to_user, amount):
        """
        Transfer rewards from one user to another.

        :param from_user: The ID of the user sending rewards.
        :param to_user: The ID of the user receiving rewards.
        :param amount: The amount to transfer.
        """
        if from_user not in self.rewards:
            raise ValueError(f"User {from_user} has no rewards.")
        
        if self.rewards[from_user] < amount:
            raise ValueError(f"User {from_user} has insufficient rewards.")
        
        if to_user not in self.rewards:
            self.rewards[to_user] = 0
        
        self.rewards[from_user] -= amount
        self.rewards[to_user] += amount

        return f"Transferred {amount} rewards from user {from_user} to user {to_user}."

    def __repr__(self):
        return f"<RewardSystem with {len(self.rewards)} users>"
