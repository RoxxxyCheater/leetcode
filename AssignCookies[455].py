#Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

#Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

 

#Example 1:

#Input: g = [1,2,3], s = [1,1]
#Output: 1
#Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
#And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
#You need to output 1.
#Example 2:

#Input: g = [1,2], s = [1,2,3]
#Output: 2
#Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
#You have 3 cookies and their sizes are big enough to gratify all of the children, 
#You need to output 2.
 

#Constraints:

#1 <= g.length <= 3 * 104
#0 <= s.length <= 3 * 104
#1 <= g[i], s[j] <= 231 - 1


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort() # сортируем список жадностей детей
        s.sort() # сортируем список размеров печенья
        i = 0 # индекс текущего ребенка
        j = 0 # индекс текущего печенья
        res = 0 # количество удовлетворенных детей
        while i < len(g) and j < len(s):
            if s[j] >= g[i]: # если размер печенья подходит для текущего ребенка
                res += 1 # увеличиваем количество удовлетворенных детей
                i += 1 # переходим к следующему ребенку
            j += 1 # переходим к следующему печенью
        return res
    

list_g = [1,2,3],[1,2]
list_s = [1,1],[1,2,3]

for index, list_g in enumerate(list_g):
    Solution.findContentChildren("Success", list_g, list_s[index])
