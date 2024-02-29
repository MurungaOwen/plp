void main() {
  List<String> names = ["owen", "hood", "great"];
  print(names[1]);
  //Maps is that consisting of key value pairs
  Map<String, int> students = {"owen": 1, "hood": 23};
  print(students);
  String rune = "Runes in Dart: \u{1F600} \u{1F64B} \u{1F680}";
  print(rune);

  int num1 = 2;
  int num2 = 4;

  print("The result is ${num2 ~/ num1}");
}
