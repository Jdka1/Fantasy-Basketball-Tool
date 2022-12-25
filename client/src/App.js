import React, { useState, useEffect } from 'react'


// BE CAREFUL WHEN SENDING TOO MANY REQUESTS


function App() {

  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/test").then(
      res => res.json()
    ).then(
      data => {
        console.log(data)
        setData(data)
      }
    )
  }, [])

  return (
    <div>
      
      {(typeof data.players === 'undefined') ? (
        <p>Loading...</p>
      ) : (
        <p>{data}</p>
      )}

    </div>
  )
}

export default App