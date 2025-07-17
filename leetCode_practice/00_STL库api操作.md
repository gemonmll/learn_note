## C++ 常用容器基础用法概述

以下按 "增 (Insert)、删 (Erase)、改 (Update)、查 (Find/Access)" 四个操作维度，梳理 `std::vector`、`std::map`、`std::set`、`std::unordered_map`、`std::deque` 的典型用法。

---

### 1. std::vector

#### 增 (Insert)
```cpp
std::vector<int> v;
v.push_back(10);                 // 在末尾插入
v.emplace_back(20);              // 原地构造并插入
v.insert(v.begin() + pos, 15);   // 在位置 pos 前插入
```

#### 删 (Erase)
```cpp
v.pop_back();                    // 删除末尾元素
v.erase(v.begin() + pos);        // 删除位置 pos 的元素
v.clear();                       // 清空所有元素
```

#### 改 (Update)
```cpp
v[2] = 99;                       // 下标访问并修改（无边界检查）
v.at(2) = 100;                   // 带边界检查的访问修改
```

#### 查 (Find/Access)
```cpp
int x = v[1];                    // 下标访问
int y = v.at(1);                 // 带边界检查
bool empty = v.empty();          // 是否为空
size_t n = v.size();             // 元素个数
```

---

### 2. std::map

#### 增 (Insert)
```cpp
std::map<std::string, int> m;
m["apple"] = 3;                // 插入或修改
m.insert({"banana", 5});       // 插入，若键已存在则不覆盖
```

#### 删 (Erase)
```cpp
m.erase("banana");             // 根据键删除元素，返回删除个数
m.clear();                     // 清空所有元素
```

#### 改 (Update)
```cpp
if (m.count("apple")) {
    m["apple"] = 10;           // 通过下标或 at 修改
    m.at("apple") = 12;
}
```

#### 查 (Find/Access)
```cpp
auto it = m.find("apple");
if (it != m.end()) {
    int val = it->second;      // 通过迭代器访问值
}
int cnt = m.count("apple");    // 存在数量 (0 或 1)
size_t sz = m.size();          // 元素总数
// C++20:
bool has = m.contains("apple");
```

---

### 3. std::set

#### 增 (Insert)
```cpp
std::set<int> s;
s.insert(3);                   // 插入元素，重复插入无效
```

#### 删 (Erase)
```cpp
s.erase(3);                    // 删除元素，返回删除个数
s.clear();                     // 清空所有
```

#### 改 (Update)
// set 中的元素不可直接修改，否则破坏排序，可通过 erase + insert 实现：
```cpp
if (s.count(3)) {
    s.erase(3);
    s.insert(4);
}
```

#### 查 (Find/Access)
```cpp
bool exists = s.count(4) > 0;  // 是否存在
auto it2 = s.find(4);
if (it2 != s.end()) {
    int v = *it2;
}
size_t len = s.size();         // 元素数量
```
#### 查询是否插入成功
返回的变量是pair，second是bool类型
``` cpp
// 尝试插入元素
auto result = mySet.insert(10);
if (result.second) {
    std::cout << "元素插入成功，值为: " << *result.first << std::endl;
} else {
    std::cout << "元素已存在，值为: " << *result.first << std::endl;
}
```

#### 使用set去重vector
```cpp
std::vector<std::vector<int>> vec2D = {
    {1, 2}, {3, 4}, {1, 2}, {5, 6}, {3, 4}
};

// 利用 set 去重
std::set<std::vector<int>> unique_set(vec2D.begin(), vec2D.end());

// 如果还想转换回 vector
std::vector<std::vector<int>> deduped(unique_set.begin(), unique_set.end());
```
#### 利用count方法判断元素是否存在
```cpp
std::set<int> s = {1, 2, 3};
std::cout << s.count(2) << std::endl; // 输出 1
std::cout << s.count(5) << std::endl; // 输出 0
```
返回值：如果 key 存在，返回 1；否则返回 0。
原因：两者都不允许重复元素，所以 count 要么是 0，要么是 1

---

### 4. std::unordered_map

#### 增 (Insert)
```cpp
#include <unordered_map>
std::unordered_map<std::string, int> um;
um["key"] = 1;                 // 插入或修改
um.insert({"foo", 42});        // 插入，不覆盖已存在
```

#### 删 (Erase)
```cpp
um.erase("foo");               // 删除键，返回删除个数
um.clear();                    // 清空所有元素
```

#### 改 (Update)
```cpp
if (um.count("key")) {
    um["key"] = 100;
    um.at("key") = 200;
}
```

#### 查 (Find/Access)
```cpp
auto it3 = um.find("key");
if (it3 != um.end()) {
    int v = it3->second;
}
int c = um.count("missing");   // 0 或 1
size_t tot = um.size();        // 元素数
```

#### 多值映射 (Key -> Multiple Values)

若一个键需要对应多个值，可使用 `std::unordered_multimap` 或将 `unordered_map` 的值类型设为容器（如 `vector`）。

**使用 unordered_multimap**
```cpp
#include <unordered_map>
std::unordered_multimap<std::string, int> umm;
umm.insert({"apple", 1});
umm.insert({"apple", 2});
umm.insert({"apple", 3});

// 查询所有 "apple" 对应的值
auto range = umm.equal_range("apple");
for (auto it = range.first; it != range.second; ++it) {
    std::cout << it->second << ' ';
}
```

**使用 unordered_map<key, vector<value>>**
```cpp
#include <unordered_map>
#include <vector>

std::unordered_map<std::string, std::vector<int>> umv;
umv["apple"].push_back(1);
umv["apple"].push_back(2);
umv["apple"].push_back(3);

// 使用 find 查找多值映射
auto it_mult = umv.find("apple");
if (it_mult != umv.end()) {
    for (int val : it_mult->second) {
        std::cout << val << ' ';
    }
} else {
    std::cout << "Key not found.";
}
```

---

### 5. std::deque

#### 增 (Insert)
```cpp
#include <deque>
std::deque<int> dq;

dq.push_back(1);               // 尾部插入
dq.push_front(0);              // 头部插入

dq.emplace_back(2);            // 尾部原地构造
dq.emplace_front(-1);          // 头部原地构造

dq.insert(dq.begin() + 2, 5);  // 在位置 2 前插入单个元素
// 插入多个相同元素
dq.insert(dq.begin(), 3, 100); // 在头部连续插入三个 100

// 插入区间 [first, last)
std::vector<int> v = {7,8,9};
dq.insert(dq.end(), v.begin(), v.end());
```

#### 删 (Erase)
```cpp
if (!dq.empty()) {
    dq.pop_back();             // 尾部删除
    dq.pop_front();            // 头部删除
}
// 删除单个位置
dq.erase(dq.begin() + 1);
// 删除区间 [first, last)
dq.erase(dq.begin(), dq.begin() + 2);

dq.clear();                   // 清空所有元素
```

#### 改 (Update)
```cpp
// 随机访问并修改
dq[2] = 50;                   // 无边界检查
dq.at(2) = 60;                // 带边界检查
// 修改首尾元素
dq.front() = 10;
dq.back() = 20;
```

#### 查 (Find/Access)
```cpp
int first = dq.front();        // 获取第一个元素
int last = dq.back();          // 获取最后一个元素
int mid = dq[3];               // 随机访问
int safe = dq.at(3);           // 带边界检查访问

size_t count = dq.size();      // 元素数量
bool isEmpty = dq.empty();     // 是否为空
```

#### 其他常用 API
```cpp
// 大小调整
dq.resize(5);                  // 改变大小，多余元素被删除，不足时插入默认值 0
dq.resize(8, 7);               // 插入默认值为 7

// 赋值
dq.assign(4, 1);               // 清空并赋值四个 1
// 范围赋值: dq.assign(v.begin(), v.end());

// 交换
deque<int> other = {100, 200};
dq.swap(other);                // 与 another 交换内容

// 迭代器
auto it_begin = dq.begin();    // 双向迭代器
for (int x : dq) std::cout << x << ' ';
```

### 6 各个容器的遍历
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <deque>

int main() {
    // 1. 遍历 std::vector
    std::vector<int> v = {1, 2, 3, 4, 5};
    std::cout << "vector: ";
    for (int x : v) std::cout << x << ' ';
    std::cout << std::endl;

    // 2. 遍历 std::map
    std::map<std::string, int> m = {{"a", 1}, {"b", 2}};
    std::cout << "map: ";
    for (const auto& [key, value] : m) std::cout << key << ':' << value << ' ';
    std::cout << std::endl;

    // 3. 遍历 std::set
    std::set<int> s = {3, 1, 4};
    std::cout << "set: ";
    for (auto it = s.begin(); it != s.end(); ++it) std::cout << *it << ' ';
    std::cout << std::endl;

    // 4. 遍历 std::unordered_map
    std::unordered_map<std::string, int> um = {{"x", 10}, {"y", 20}};
    std::cout << "unordered_map: ";
    for (auto it = um.begin(); it != um.end(); ++it) std::cout << it->first << ':' << it->second << ' ';
    std::cout << std::endl;

    // 5. 遍历 std::deque
    std::deque<int> dq = {7, 8, 9};
    std::cout << "deque: ";
    for (auto it = dq.begin(); it != dq.end(); ++it) std::cout << *it << ' ';
    std::cout << std::endl;

    return 0;
}
```
### 7 各个容器间的排序
```cpp
#include <algorithm>    // std::sort, std::stable_sort
#include <iostream>
#include <vector>
#include <deque>
#include <list>
#include <array>
#include <string>

struct Person {
    std::string name;
    int age;
};

int main() {
    // 1. 排序 std::vector<int>
    std::vector<int> v = {5, 2, 9, 1, 5, 6};
    std::sort(v.begin(), v.end());  // 升序
    // std::sort(v.begin(), v.end(), std::greater<int>()); // 降序

    std::cout << "sorted vector: ";
    for (int x : v) std::cout << x << ' ';
    std::cout << "\n\n";

    // 2. 排序 std::deque<int>
    std::deque<int> dq = {3, 7, 4, 1, 8};
    std::sort(dq.begin(), dq.end());  // deque 也支持随机访问迭代器
    std::cout << "sorted deque: ";
    for (int x : dq) std::cout << x << ' ';
    std::cout << "\n\n";

    // 3. 排序 std::array<int, N>
    std::array<int,5> arr = {10, 3, 5, 7, 2};
    std::sort(arr.begin(), arr.end());
    std::cout << "sorted array: ";
    for (int x : arr) std::cout << x << ' ';
    std::cout << "\n\n";

    // 4. 排序 std::list<int> —— list 只能用成员函数 .sort()
    std::list<int> lst = {4, 2, 5, 1, 3};
    lst.sort();  // 升序
    // lst.sort(std::greater<int>()); // 降序
    std::cout << "sorted list: ";
    for (int x : lst) std::cout << x << ' ';
    std::cout << "\n\n";

    // 5. 对自定义结构体排序
    std::vector<Person> people = {
        {"Alice", 30}, {"Bob", 25}, {"Charlie", 35}
    };
    // 按 age 升序
    std::sort(people.begin(), people.end(),
        [](auto &a, auto &b) { return a.age < b.age; });
    std::cout << "people sorted by age:\n";
    for (auto &p : people) {
        std::cout << "  " << p.name << " (" << p.age << ")\n";
    }
    std::cout << "\n";

    // 稳定排序：保持相等元素的相对顺序
    std::vector<int> v2 = {3, 1, 4, 1, 5, 9, 2, 6, 5};
    std::stable_sort(v2.begin(), v2.end());
    std::cout << "stable_sorted vector: ";
    for (int x : v2) std::cout << x << ' ';
    std::cout << "\n";

    return 0;
}
```


## 8 构造函数

#### 8.1.直接拷贝（Copy Constructor / 赋值运算符）
```cpp
#include <vector>
#include <iostream>

int main() {
    std::vector<int> src = {1, 2, 3, 4, 5};

    // 方法 A：拷贝构造
    std::vector<int> dst1(src);

    // 方法 B：赋值
    std::vector<int> dst2;
    dst2 = src;

    // 输出验证
    for (int x : dst1) std::cout << x << ' ';
    std::cout << std::endl;
    for (int x : dst2) std::cout << x << ' ';
    std::cout << std::endl;

    return 0;
}
```
#### 8.2.区间拷贝
``` cpp
#include <vector>
#include <iostream>

int main() {
    std::vector<int> src = {10, 20, 30, 40, 50};

    // 拷贝下标 [1, 4) 的元素：20, 30, 40
    std::vector<int> part(src.begin() + 1, src.begin() + 4);

    for (int x : part) std::cout << x << ' ';  // 输出：20 30 40
    std::cout << std::endl;

    return 0;
}
```
#### 8.3.算法拷贝
```cpp
#include <vector>
#include <algorithm>
#include <iterator>

int main() {
    std::vector<int> src = {1, 2, 3, 4, 5, 6};

    // 完整拷贝
    std::vector<int> dst1(src.size());
    std::copy(src.begin(), src.end(), dst1.begin());

    // 带条件拷贝（只拷贝偶数）
    std::vector<int> dst2;
    std::copy_if(src.begin(), src.end(), std::back_inserter(dst2),
                 [](int x) { return x % 2 == 0; });

    // 元素变换生成（每个元素乘以 10）
    std::vector<int> dst3;
    std::transform(src.begin(), src.end(), std::back_inserter(dst3),
                   [](int x) { return x * 10; });

    return 0;
}
```
#### 8.4 移动语义（避免拷贝开销）
``` cpp
#include <vector>
#include <string>
#include <iostream>

int main() {
    std::vector<std::string> src = {"a", "b", "c"};

    // 预分配空间
    std::vector<std::string> dst;
    dst.reserve(src.size());

    // 将 src 中的字符串移动到 dst
    for (auto &s : src) {
        dst.push_back(std::move(s));
    }

    // 输出验证
    for (auto &s : dst) std::cout << s << ' ';  // 输出 a b c
    std::cout << std::endl;

    return 0;
}

```

#### 8.5 填充构造（基于大小和默认值）

```cpp
#include <vector>

// 构造一个与 src 等长，但全部初始化为 -1 的 vector
std::vector<int> src = {1, 2, 3, 4};
std::vector<int> dst(src.size(), -1);  // {-1, -1, -1, -1}

```

## 9 C++ `std::string` 常见用法

#### 9.1. 创建与赋值
```cpp
#include <string>

// 直接初始化
std::string s1 = "Hello";
std::string s2("World");

// 重复字符构造
std::string s3(5, 'x'); // "xxxxx"

// 从子串或 C 字符串构造
const char* cstr = "example";
std::string s4(cstr + 2, 4); // "amp"
std::string s5(cstr, cstr + 3); // "exa"

// 拷贝与赋值
std::string s6 = s1;      // 拷贝构造
s2 = s1;                  // 赋值
```

#### 9.2. 拼接与追加
```cpp
std::string a = "Hello, ";
std::string b = "world!";

// operator+
std::string c = a + b;    // "Hello, world!"

// append
a.append(b);              // a == "Hello, world!"
a += " Nice to meet you."; // a += ...
```

#### 9.3. 访问字符
```cpp
std::string s = "ABCDE";

// 下标访问（无边界检查）
char c0 = s[0];           // 'A'

// at()（带检查，越界会抛 out_of_range）
char c1 = s.at(1);        // 'B'

// front() / back()
char first = s.front();   // 'A'
char last  = s.back();    // 'E'
```

#### 9.4. 子串与截取
```cpp
std::string s = "Hello, world!";

// substr(pos, len)
std::string sub1 = s.substr(7, 5); // "world"

// 从 pos 到末尾
std::string sub2 = s.substr(7);    // "world!"
```

#### 9.5. 查找与替换
```cpp
std::string s = "ababcdabab";

// find / rfind
size_t pos1 = s.find("ab");     // 0
size_t pos2 = s.find("ab", 2);  // 2
size_t pos3 = s.rfind("ab");    // 6
bool notFound = (s.find("zz") == std::string::npos);

// replace(pos, len, newStr)
s.replace(0, 2, "xy");          // "xyabcdabab"
```

#### 9.6. 比较
```cpp
std::string s1 = "apple";
std::string s2 = "banana";

// operator==, !=, <, >, <=, >=
bool eq = (s1 == s2);           // false
bool lt = (s1 < s2);            // true (字典序)

// compare()
int cmp = s1.compare(s2);       // <0 表示 s1<s2
```

#### 9.7. 转换与 C 字符串接口
```cpp
std::string s = "12345";

// to_string / stoi / stol / stof 等
int n = std::stoi(s);           // 12345
double d = std::stod("3.14");   // 3.14

// c_str() / data()
const char* p = s.c_str();      // 以 '\0' 结尾
char* q = &s[0];                // 可写（C++17 后保证连续）
```

#### 9.8. 输入／输出
```cpp
#include <iostream>
#include <sstream>

// std::cin
std::string line;
std::getline(std::cin, line);

// std::stringstream
std::stringstream ss("10 20 30");
int x, y, z;
ss >> x >> y >> z;              // x=10, y=20, z=30

// std::cout
std::cout << line << std::endl;
```

#### 9.9. 遍历与迭代器
```cpp
std::string s = "hello";

// 范围 for
for (char c : s) {
    std::cout << c << ' ';
}

// 迭代器
for (auto it = s.begin(); it != s.end(); ++it) {
    std::cout << *it << ' ';
}
```

#### 9.10. 大小与容量
```cpp
std::string s = "hello";

// 大小与检查
size_t len = s.length();        // 或 s.size()
bool empty = s.empty();

// 修改大小
s.reserve(100);                 // 预留容量
s.resize(3);                    // s == "hel"
s.shrink_to_fit();              // 收缩容量到当前大小
```
#### 9.11 与c字符串的关系
string不是靠 '\0' 结束的，std::string 内部保存了自己的长度。具体来说：
std::string 维护了一个长度字段和一个指向字符缓冲区的指针，所以它并不需要也不依赖于末尾的 '\0' 来判断字符串结束。
你可以在 std::string 中存放任意字符，包括 '\0'，它会当作普通字符对待：
```cpp
std::string s = std::string("ab\0cd", 5);
// s.size() == 5，内容是 ['a','b','\0','c','d']
```
当你需要得到 C 风格的以 '\0' 结尾的字符串时，可以调用：
s.c_str()：返回一个以 '\0' 结尾的 const char*
s.data()（C++17 起保证返回的也是以 '\0' 结尾的指针）
示例：
```cpp
int main() {
    std::string s = "hello";
    const char* p = s.c_str();
    std::cout << "C‑string: " << p << std::endl;     // 输出 hello
    std::cout << "长度: " << s.size() << std::endl;  // 输出 5

    // 内部可以包含 '\0'
    std::string t = std::string("ab\0cd", 5);
    std::cout << "t.size() = " << t.size() << std::endl;        // 5
    std::cout << "t.c_str() 长度是 " << std::strlen(t.c_str())  // 2
              << "（遇到第一个 '\\0' 就停止）" << std::endl;
    return 0;
}
```
