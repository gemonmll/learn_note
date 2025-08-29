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
#### 初始化 指定大小并且提供初始值
```cpp
std::vector<int> v(10,0);//10个元素，每个都是5
std::vector<int> v = {1,2,3,4,5};
```
#### 一些注意事项
> 在 C++ 中，std::vector 提供了一个成员函数 end()，它返回一个指向容器末尾元素的迭代器。值得注意的是，end() 返回的迭代器并不指向最后一个元素，而是指向容器“末尾之后”的位置，也就是最后一个元素之后的位置。换句话说，它是容器中最后一个元素之后的位置的一个迭代器。
> 如果你想通过索引来访问 std::vector 的最后一个元素，你可以使用 size() 成员函数来获取容器的大小，然后通过 size() - 1 来获取最后一个元素的索引。
> std::vector 的 .begin() 函数用于获取指向第一个元素的迭代器。 ‌在 C++ 标准模板库（STL）中，std::vector 的 .begin() 成员函数返回一个指向容器第一个元素的迭代器。该迭代器可用于遍历整个容器元素。若容器为空，.begin() 和 .end() 返回的迭代器会相等。

**一些常用api**
> 1、v.front() / v.back()：直接访问首尾元素。
> 2、v[0] / v[v.size()-1]：下标访问，不做越界检查。
> 3、v.at(0) / v.at(v.size()-1)：带越界检查，越界时会抛出 std::out_of_range。 ‌
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
### 优先队列
>1、定义：优先队列是一种特殊的队列，出队顺序不再是“先进先出”，而是按“优先级”进行——每次出队的都是当前队列中“优先级最高”（或最低）的元素。
> 2、在 C++ STL 中，std::priority_queue 默认实现成最大堆，即 top() 返回容器中最大的元素。
> 3、模板如下：
T：存储元素的类型
Container：底层容器类型，需要支持随机访问迭代器（默认 std::vector<T>）
Compare：比较谓词，默认用 std::less，形成最大堆；若想最小堆，可用 std::greater 或自定义
```cpp
template<
    class T,
    class Container = std::vector<T>,
    class Compare = std::less<typename Container::value_type>
>
class priority_queue;
```
**常用方法**
| 方法                                  | 功能            | 复杂度      |
| ----------------------------------- | ------------- | -------- |
| `empty()`                           | 判断是否为空        | O(1)     |
| `size()`                            | 返回元素个数        | O(1)     |
| `top()`                             | 访问当前“最高优先级”元素 | O(1)     |
| `push(const T& x)` / `emplace(...)` | 插入新元素         | O(log n) |
| `pop()`                             | 弹出当前“最高优先级”元素 | O(log n) |
| `swap(other)`                       | 与另一个优先队列交换    | 平摊 O(1)  |


**构建最大堆**
```cpp
#include <queue>
#include <vector>
#include <iostream>

int main() {
    std::priority_queue<int> pq;
    pq.push(3);
    pq.push(1);
    pq.push(4);
    std::cout << pq.top(); // 输出 4
}
```
**仿函数构建最小堆**
```cpp
// 仿函数
struct MyCmp {
    bool operator()(int a, int b) const {
        return a > b; // 小的“优先”→最小堆
    }
};
std::priority_queue<int, std::vector<int>, MyCmp> pq1;

// Lambda + decltype
auto cmp = [](int a, int b){ return a > b; };
std::priority_queue<int, std::vector<int>, decltype(cmp)> pq2(cmp);

// 函数指针
bool fncmp(int a, int b){ return a > b; }
std::priority_queue<int, std::vector<int>, bool(*)(int,int)> pq3(fncmp);
```
>**堆元素删除---延迟删除法**
> 当你需要“删除指定值”但不想重建整个堆时，可以配合一个 unordered_map<int,int> 来标记要删除的元素，真正遇到时再 pop 掉
```cpp
void clean() {
        while (!pq.empty()) {
            auto it = to_remove.find(pq.top());
            if (it != to_remove.end()) {
                pq.pop();
                if (--it->second == 0) to_remove.erase(it);
            } else {
                break;
            }
        }
    }
```
**利用pair进行延迟消除**
```cpp
	//239 滑动窗口最大值
	vector<int> maxSlidingWindow(vector<int>& nums, int k) {
		priority_queue<pair<int, int>> slideQueue;
		vector<int> resVec;
		if (nums.size() < k)
			return resVec;

		//构建堆
		for (int i = 0; i < k; i++)
		{
			pair<int, int> t(nums[i],i);
			slideQueue.push(t);
		}
		resVec.push_back(slideQueue.top().first);

		//生成最大值
		for (int i = k ; i < nums.size(); i++)
		{
			pair<int, int> t(nums[i], i);
			slideQueue.push(t);
			
			while (slideQueue.top().second <= i - k)
			{
				slideQueue.pop();
			}
			resVec.push_back(slideQueue.top().first);
		}

		return resVec;
	}
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
### 10 仿函数 vs 函数指针 vs 匿名函数
>
| 比较项     | 仿函数                   | 匿名函数（Lambda）                   |
| ------- | --------------------- | ------------------------------ |
| 定义方式    | 定义类并重载 `operator()`   | 使用 `[](){}` 的语法                |
| 是否命名    | ✅ 需要命名类               | ✅ 可赋给变量，但本体匿名                  |
| 写法简洁性   | ❌ 繁琐（需要 struct/class） | ✅ 简洁、内联                        |
| 可否捕获状态  | ✅ 通过构造函数              | ✅ 通过 `[=]`, `[&]`, `[x]` 等捕获机制 |
| 类型名称    | 有名字（类名）               | 无类型名，使用 `auto` 推导              |
| 可否嵌套    | ❌ 不易嵌套                | ✅ 可以直接嵌套                       |
| 推荐场景    | 可重用、有多个函数逻辑的复杂对象      | 简洁临时函数、STL 参数等                 |
| C++支持版本 | C++98 起               | C++11 起                        |

>
| 项目      | 仿函数（Functor）                 | 函数指针（Function Pointer） |
| ------- | ---------------------------- | ---------------------- |
| 本质      | 是一个**类的对象**，重载了 `operator()` | 是一个指向函数的变量             |
| 是否可携带状态 | ✅ 可以有成员变量，保存状态               | ❌ 不能保存状态（仅指向函数地址）      |
| 性能优化    | ✅ 编译器能内联优化                   | ❌ 难以内联优化               |
| 灵活性     | ✅ 可封装任意复杂行为                  | ❌ 限于函数已有逻辑             |
| 现代用途    | STL 容器操作、算法传参                | C 风格 API，或者需要简单函数回调的场景 |
> **仿函数 一些示例**
> **实例 1：用于排序的仿函数**
``` cpp
#include <vector>
#include <algorithm>
#include <iostream>

struct DescendCompare {
    bool operator()(int a, int b) const {
        return a > b; // 降序排列
    }
};

int main() {
    std::vector<int> v = {3, 1, 4, 2};
    std::sort(v.begin(), v.end(), DescendCompare()); // 使用仿函数排序

    for (int x : v) std::cout << x << " "; // 输出：4 3 2 1
}
```
**实例 2：自定义优先队列比较器（最小堆**
```cpp
#include <queue>
#include <vector>
#include <iostream>

struct MinHeap {
    bool operator()(int a, int b) const {
        return a > b; // 构造最小堆
    }
};

int main() {
    std::priority_queue<int, std::vector<int>, MinHeap> pq;
    pq.push(3); pq.push(1); pq.push(5);

    while (!pq.empty()) {
        std::cout << pq.top() << " ";
        pq.pop();
    }
    // 输出：1 3 5
}

```
**实例 3：自定义优先队列比较器（最小堆）匿名函数**
>不能直接写 cmp，因为模板需要类型名，你只能用 decltype(cmp) 来拿到它的类型，或者改用 std::function。
```cpp
#include <iostream>
#include <queue>
#include <vector>
#include <functional>
int main() {
    // 用 lambda 表达式定义最小堆比较器（小的优先）
    auto cmp = [](int a, int b) {
        return a > b; // "大"的在前 => 小根堆
    };

    // priority_queue 使用 vector 容器 + 比较器（注意第三个参数）
    std::priority_queue<int, std::vector<int>, decltype(cmp)> minHeap(cmp);

    // 插入元素
    minHeap.push(5);
    minHeap.push(1);
    minHeap.push(10);
    minHeap.push(3);

    // 输出元素（从小到大）
    while (!minHeap.empty()) {
        std::cout << minHeap.top() << " ";
        minHeap.pop();
    }
    // 输出：1 3 5 10

    return 0;
}

```
**std::function构建最小堆**
```cpp
auto minHeap = std::priority_queue<
    int,
    std::vector<int>,
    std::function<bool(int, int)>
>(
    [](int a, int b) { return a > b; }  // 最小堆比较器
);
```

**std::function和仿函数**
| 特性       | 仿函数（functor）           | `std::function`     |
| -------- | ---------------------- | ------------------- |
| 类型       | 自定义类型                  | 模板类                 |
| 灵活性      | 高，可保存状态、模板化            | 更高，可存储任意可调用对象       |
| 使用场景     | STL 比较器、自定义策略、性能要求高的场合 | 回调、泛型接口、动态函数绑定等     |
| 是否支持类型擦除 | ❌ 不支持                  | ✅ 支持                |
| 性能       | ✅ 通常更快，尤其是 inline 场景   | ❌ 稍慢，有额外开销（内存、间接调用） |
| 可否捕获状态   | ✅ 可（类成员）               | ✅ 可（闭包也支持）          |
| 用法复杂度    | 中（要写结构体或类）             | 简（直接赋 lambda 或函数）   |

>s td::function 是一个 通用的函数封装器，可以存储：
普通函数、函数指针、Lambda 表达式、仿函数对象
```cpp
#include <functional>
#include <iostream>

bool compare(int a, int b) {
    return a > b;
}

int main() {
    std::function<bool(int, int)> f = compare;         // 普通函数
    std::function<bool(int, int)> g = [](int a, int b) { return a > b; }; // lambda

    std::cout << f(3, 2) << "\n";  // 输出 1
    std::cout << g(3, 2) << "\n";  // 输出 1
}
```
### 11 一些其余知识
> std::pair<int,int> 类似于一个struct，里面都是int类型
```cpp
template< class T1, class T2 >
struct pair {
    T1 first;
    T2 second;
    // 构造函数、赋值操作符、比较运算符等
};
```