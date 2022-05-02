import React from 'react'
import Header from './components/Header'
import icon from './SwiftIcon.png'

const App = () => {
  console.log(icon);

  return (
    <div>
      <Header icon={icon}/>
    </div>
  )
}

export default App