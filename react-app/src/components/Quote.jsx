function Quote({text, author}) {
    return (
        <div className="quote-container">
            <p className="quote-text">{text}</p>
            <p className="quote-author">{author}</p>
      </div>
    );
}

export default Quote;