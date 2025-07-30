import React from 'react';
import { PieChart, Pie, Cell } from 'recharts';
const data = [ { name: 'Loss', value: 9 }, { name: 'Gain', value: 20 }, { name: 'Total', value: 30 } ];
const COLORS = ['#9CA3AF','#34D399','#FBBF24'];
export default function IPOOverviewChart() {
  return (
    <PieChart width={300} height={200}>
      <Pie data={data} dataKey="value" cx="50%" cy="50%" innerRadius={50} outerRadius={80}>
        {data.map((_, i) => <Cell key={i} fill={COLORS[i]} />)}
      </Pie>
    </PieChart>
  );
}
