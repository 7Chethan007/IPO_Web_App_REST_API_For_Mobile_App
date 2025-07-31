const fs = require('fs');
const path = require('path');

function listDirectory(dir, prefix = '') {
  const items = fs.readdirSync(dir);
  
  items.forEach((item, index) => {
    if (item === 'node_modules' || item === 'dist') return;
    
    const fullPath = path.join(dir, item);
    const isLast = index === items.length - 1;
    const currentPrefix = isLast ? '└── ' : '├── ';
    const nextPrefix = isLast ? '    ' : '│   ';
    
    console.log(prefix + currentPrefix + item);
    
    if (fs.statSync(fullPath).isDirectory()) {
      listDirectory(fullPath, prefix + nextPrefix);
    }
  });
}

console.log('ipo_apps/');
listDirectory('./');