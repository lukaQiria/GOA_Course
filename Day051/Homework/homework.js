function Car(brand) {
    this.brand = brand;
}

function Student(name, age, grade) {
    this.name = name;
    this.age = age;
    this.grade = grade;
}

let student1 = new Student("Luka", 16, "A");
let student2 = new Student("Giorgi", 17, "B");


console.log(student1.name);   
console.log(student2.grade); 