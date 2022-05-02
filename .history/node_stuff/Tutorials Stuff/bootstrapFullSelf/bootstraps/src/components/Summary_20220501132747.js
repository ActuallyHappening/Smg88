import React from 'react'

const Summary = ({ numTasks, numReminders }) => {
  return (
    <div className="text-centertext-light">
      <p className="alert alert-info">
        Summary: {numTasks ? numTasks : "no"} tasks and {numReminders ? numReminders : "no"} active reminders
      </p>
    </div>
  )
}

export default Summary