import React, { useState, useEffect } from 'react';
import { getMarketplaceListings } from '../api/rest';

const Marketplace: React.FC = () => {
    const [listings, setListings] = useState<any[]>([]);

    useEffect(() => {
        getMarketplaceListings().then(data => setListings(data));
    }, []);

    return (
        <div>
            <h2>Agent Marketplace</h2>
            {listings.map((item, index) => (
                <div key={index} style={{border: '1px solid #ccc', margin: '10px'}}>
                    <p>Dataset: {item.name}</p>
                    <p>Price: {item.price} COIN</p>
                    <button>Buy</button>
                </div>
            ))}
        </div>
    );
}

export default Marketplace;
