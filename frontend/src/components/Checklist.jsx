import React, { useState, useEffect } from 'react';
import { fetchChecklist } from '../api/api';

const Checklist = () => {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadChecklist = async () => {
      const data = await fetchChecklist();
      setItems(data.items);
      setLoading(false);
    };
    loadChecklist();
  }, []);

  const toggleItem = (id) => {
    setItems(items.map(item => 
      item.id === id ? { ...item, completed: !item.completed } : item
    ));
  };

  return (
    <section className="section">
      <h3>Your Health Checklist</h3>
      {loading ? (
        <p>Loading checklist...</p>
      ) : (
        <div className="card-list">
          {items.map((item) => (
            <div key={item.id} className="checklist-item">
              <input 
                type="checkbox" 
                checked={item.completed} 
                onChange={() => toggleItem(item.id)}
                id={`check-${item.id}`}
              />
              <label 
                htmlFor={`check-${item.id}`} 
                style={{ textDecoration: item.completed ? 'line-through' : 'none', color: item.completed ? '#666' : 'inherit', cursor: 'pointer' }}
              >
                {item.task}
              </label>
            </div>
          ))}
        </div>
      )}
    </section>
  );
};

export default Checklist;
