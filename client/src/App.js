import React, { useState, useEffect } from 'react'


// BE CAREFUL WHEN SENDING TOO MANY REQUESTS


function App() {

  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/per_game_averages/2023").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  return (
    <div>

      {(typeof data.per_game_averages === 'undefined') ? (
        <p>Loading Data...</p>
      ) : (
        <pre>{JSON.stringify(data.per_game_averages, null, " ")}</pre>
      )}

    </div>
  )
}

export default App