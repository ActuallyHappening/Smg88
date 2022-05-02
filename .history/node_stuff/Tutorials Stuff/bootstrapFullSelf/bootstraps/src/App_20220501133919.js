import React from 'react'
import Header from './components/Header'
import icon from "./Swift Icon.png"

const App = () => {
  console.log(icon);

  return (
    <div>
      <Header icon={icon}/>
    </div>
  )
}

export default App