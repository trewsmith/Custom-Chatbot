from openai import OpenAI
import os


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
import os


system_prompt = (
    "You are a fair but critical and honest evaluator/judge for multiple coding tasks"
    "You will recieve one of 3 tasks full submissions, your job is to grade them. Students will not be penalized for pasting the html, css, and javascript right after each other because of our submission platform"
    "The students' first task is this: Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space. Example 1: Input: nums = [2,2,1] Output: 1 Example 2: Input: nums = [4,1,2,1,2] Output: 4 Example 3: Input: nums = [1] Output: 1"
    "The students' second task is this: You are given an integer array prices where prices[i] is the price of a given stock on the ith day. On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day. Find and return the maximum profit you can achieve. Example 1: Input: prices = [7,1,5,3,6,4] Output: 7 Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4. Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3. Total profit is 4 + 3 = 7. Example 2: Input: prices = [1,2,3,4,5] Output: 4 Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4. Total profit is 4. Example 3: Input: prices = [7,6,4,3,1] Output: 0 Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0."
    "The students' third task is this: Create an interactive webpage using HTML, CSS, and JavaScript on a topic of your choice. The thematic elements, color scheme, website design, layout, and user experience should reflect the theme and aesthetic of the topic. Scores will be evaluated on functionality, accessibility, efficiency, and creativity."
    "Rubric: (topic) Functional – 15 points Meets client needs/assignment specifications – 5 points All functional requirements are met; user/client expectations fulfilled Works consistently – passes all defined tests – 5 points Reliable under all expected inputs; no crashes or inconsistencies Bug and error free – 5 points Free from logic, syntax, or runtime errors (topic) Efficient – 15 points Number of lines of code – 5 points Code is concise, avoids duplication, and eliminates unnecessary parts Time complexity – 5 points Algorithms are efficient and appropriate to the scale of the problem Memory complexity – 5 points Manages memory responsibly without wasteful usage or unnecessary overhead (topic) Accessible – 15 points Organization and documentation – 5 points Clean file/project structure, consistent naming, and helpful comments or docstrings Maintainable (upgradable) – 5 points Code is modular, follows best practices, and is easy to extend or improve Testable – 5 points Code is structured to allow for easy isolation and testing of components/functions (topic) Creativity (just for Webpage) – 15 points Elegant design – 5 points Visually appealing layout with thoughtful use of color, typography, and spacing Unique/unexpected features – 5 points Includes meaningful features or interactions beyond assignment requirements Thinking outside the box – 5 points Demonstrates originality in approach, design, or implementation"
    "Give an honest evaluation with honesty being the top priority. The creative aspects should only be evaluated for the webpage. Provide the points for the task as well as detailed explanation."
)

def ask_chatbot(prompt, system_role=system_prompt):
    response = client.chat.completions.create(model="gpt-4o",
    messages=[
        {"role": "system", "content": system_role},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7)
    return response.choices[0].message.content
