class Solution:
    def nextLargerElement(self,arr,n):
        st=[arr[-1]]
        l=len(arr)
        ind=l-2
        t=[-1]*l
        for i in range(2,l+1):
            x=0
            if st[-1]>arr[l-i]:
                t[ind]=st[-1]
                st.append(arr[l-i])
            else:
                while st[-1]<=arr[l-i]:
                    st.pop()
                    if st==[]:
                        x=1
                        t[ind]=-1
                        break
                if x==0:
                    t[ind]=st[-1]
                st.append(arr[l-i])
            ind-=1
        return t
                
