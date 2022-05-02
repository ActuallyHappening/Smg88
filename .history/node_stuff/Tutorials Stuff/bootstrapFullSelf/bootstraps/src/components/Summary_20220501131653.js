import React from 'react'

const Summary = ({ numTasks, numReminders }) => {
  return (
    <div>Summary: {numTasks} tasks and {numReminders} active reminders</div>
  )
}

export default Summary