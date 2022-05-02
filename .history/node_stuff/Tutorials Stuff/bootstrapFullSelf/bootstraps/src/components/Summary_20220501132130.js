import React from 'react'

const Summary = ({ numTasks, numReminders }) => {
  return (
    <div className="position-sticky text-center bg-primary text-light p-.5%">
      <h2>
        Summary: {numTasks ? numTasks : "no"} tasks and {numReminders ? numReminders : "no"} active reminders
      </h2>
    </div>
  )
}

export default Summary