import React from 'react'

const Summary = ({ numTasks, numReminders }) => {
  return (
    <div>Summary: {numTasks ? numTasks : "no"} tasks and {numReminders ? numReminders : "no"} active reminders</div>
  )
}

export default Summary