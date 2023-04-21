import './App.css';
import Quote from './components/Quote.jsx';
import React, { useEffect, useState } from 'react';

function App() {
  const [quote, setQuote] = useState({text: '', author: ''});

  useEffect(() => {
    fetch('26.22.125.216:8080/api')
      .then(res => res.json())
      .then(obj => console.log(obj));
      //.then(obj => setQuote({text: obj.text, author: obj.author}));
  }, [])

  return (
    <div className="App">
      <Quote text={quote.text} author={quote.author}/>
    </div>
  );
}

export default App;