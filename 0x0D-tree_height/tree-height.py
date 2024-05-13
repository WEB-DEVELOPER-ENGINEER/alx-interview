def compute_height(n, parents):
    heights = [0] * n
    def dfs(node):
        stack = [node]
        while stack:
            current_node = stack[-1]
            if heights[current_node] != 0:
                stack.pop()
            elif parents[current_node] == -1:
                heights[current_node] = 1
                stack.pop()
            else:
                parent_node = parents[current_node]
                if heights[parent_node] == 0:
                    stack.append(parent_node)
                else:
                    heights[current_node] = heights[parent_node] + 1
                    stack.pop()
    for node in range(n):
        dfs(node)
    max_height = max(heights)
    return max_height

if __name__ == "__main__":
    n = int(input().strip())
    parents = list(map(int, input().strip().split()))
    print(compute_height(n, parents))