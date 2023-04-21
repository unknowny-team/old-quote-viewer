import './App.css';
import Quote from './components/Quote.jsx';
import React, { useEffect, useState } from 'react';

function App() {
  const [quote, setQuote] = useState({text: '', author: ''});

  useEffect(() => {
    fetch('http://26.22.125.216:5000/api', {
      method: 'GET',
      mode: 'cors',
      headers: {'Content-Type': 'application/json'},
    })
      .then(res => {
        if (res.ok)
          return res.json().then(obj => setQuote({text: obj.text, author: obj.author}));
        else
          return res.json().then(obj => console.log(`[Server ERROR] ${obj.error}`));
      })
  }, [])

  return (
    <div className="App">
      {quote.text !== '' && quote.author !== ''
        ? <Quote text={quote.text} author={quote.author}/> 
        : <h3 className="quote-container">Цитата не загружена...</h3>}
    </div>
  );
}

export default App;