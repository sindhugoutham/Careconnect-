const API_BASE_URL = 'http://localhost:8000/api';

export const askPolicyQuestion = async (question) => {
  try {
    const response = await fetch(`${API_BASE_URL}/policy/ask`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ question }),
    });
    if (!response.ok) throw new Error('Network response was not ok');
    return await response.json();
  } catch (error) {
    console.error('Error asking policy question:', error);
    return { answer: 'Sorry, there was an error processing your request.' };
  }
};

export const fetchChecklist = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/checklist/`);
    if (!response.ok) throw new Error('Network response was not ok');
    return await response.json();
  } catch (error) {
    console.error('Error fetching checklist:', error);
    return { items: [] };
  }
};

export const findCare = async (location, need) => {
  try {
    const response = await fetch(`${API_BASE_URL}/care/find`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ location, need }),
    });
    if (!response.ok) throw new Error('Network response was not ok');
    return await response.json();
  } catch (error) {
    console.error('Error finding care:', error);
    return { results: [] };
  }
};
