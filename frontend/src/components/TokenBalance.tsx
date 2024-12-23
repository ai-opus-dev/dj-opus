import React, { useEffect, useState } from 'react';
import { ethers } from 'ethers';

interface TokenBalanceProps {
  address: string;
  tokenAddress: string;
}

const TokenBalance: React.FC<TokenBalanceProps> = ({ address, tokenAddress }) => {
  const [balance, setBalance] = useState<string>('0');

  useEffect(() => {
    const fetchBalance = async () => {
      if (address && tokenAddress) {
        const provider = new ethers.JsonRpcProvider(); // Replace with your RPC provider
        const tokenContract = new ethers.Contract(
          tokenAddress,
          ['function balanceOf(address) view returns (uint256)'],
          provider
        );

        const balance = await tokenContract.balanceOf(address);
        setBalance(ethers.utils.formatUnits(balance, 18)); // Adjust decimal precision as needed
      }
    };

    fetchBalance();
  }, [address, tokenAddress]);

  return (
    <div>
      <h3>Token Balance</h3>
      <p>Address: {address}</p>
      <p>Balance: {balance}</p>
    </div>
  );
};

export default TokenBalance;
