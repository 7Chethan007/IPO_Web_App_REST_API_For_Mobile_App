import React from 'react';
import { Doughnut } from 'react-chartjs-2';
export default function MainBoardChart() {
  const data = {
    labels: ['Upcoming', 'New Listed', 'Ongoing'],
    datasets: [{ data: [15,25,2], backgroundColor: ['#C7D2FE','#A5B4FC','#E0E7FF'] }]
  };
  return <Doughnut data={data} />;
}