import React, { useState } from 'react';
import { findCare } from '../api/api';

const FindCare = () => {
  const [location, setLocation] = useState('');
  const [need, setNeed] = useState('');
  const [results, setResults] = useState([]);
  const [searched, setSearched] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleSearch = async (e) => {
    e.preventDefault();
    if (!location.trim() || !need.trim()) return;

    setLoading(true);
    const data = await findCare(location, need);
    setResults(data.results);
    setSearched(true);
    setLoading(false);
  };

  return (
    <section className="section">
      <h3>Find Care</h3>
      <form onSubmit={handleSearch} className="form-group" style={{ flexDirection: 'column', gap: '1rem' }}>
        <div style={{ display: 'flex', gap: '1rem' }}>
          <input 
            type="text" 
            value={location} 
            onChange={(e) => setLocation(e.target.value)} 
            placeholder="Zip code or City..."
            required
          />
          <input 
            type="text" 
            value={need} 
            onChange={(e) => setNeed(e.target.value)} 
            placeholder="Specialty (e.g., Cardiology, General)..."
            required
          />
        </div>
        <button type="submit" disabled={loading}>
          {loading ? 'Searching...' : 'Search Options'}
        </button>
      </form>
      
      {searched && (
        <div className="card-list" style={{ marginTop: '1rem' }}>
          {results.length > 0 ? (
            results.map((item) => (
              <div key={item.id} className="card">
                <h4>{item.name}</h4>
                <p><strong>Type:</strong> {item.type}</p>
                <p><strong>Specialty:</strong> {item.specialty}</p>
                <p><strong>Address:</strong> {item.address}</p>
              </div>
            ))
          ) : (
            <p>No results found for your search.</p>
          )}
        </div>
      )}
    </section>
  );
};

export default FindCare;
