const students = [...document.querySelectorAll(".name")].map(
  (person) => person.innerText.split(" ")[0]
);

const rooms = [];
for (let i = 0; i < students.length; i += 2) {
  const pairs = students.slice(i, i + 2);
  if (pairs.length < 2) {
    rooms.at(-1).push(students[i]);
    continue;
  }
  rooms.push(pairs);
}

const roomNames = rooms.map((room, index) => {
  return `Room ${index + 1}: ${room.join(" - ")}`;
});

console.log(roomNames);
