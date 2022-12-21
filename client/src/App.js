import React, { useState, useEffect } from 'react'

function App() {

  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/data").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
      }
    )
  }, [])

  return (
    <div>
      
      {(typeof data.players === 'undefined') ? (
        <p>Loading...</p>
      ) : (
        // <p>{JSON.stringify(data.players, null, "")}</p>
        <pre>{JSON.stringify(data.players, null, "  ")}</pre>
      )}

    </div>
  )
}

export default App