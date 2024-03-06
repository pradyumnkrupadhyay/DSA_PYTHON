class Solution:
    def simplifyPath(self, path: str) -> str:
        path_stack = []
        for s in path.split("/"):
            if not s:
                continue
            elif s == ".":
                continue
            elif s == "..":
                if path_stack:
                    path_stack.pop()
            else:
                path_stack.append(s)
        return "/" + "/".join(path_stack)
        