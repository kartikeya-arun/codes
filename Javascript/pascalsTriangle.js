/**
 * @param {number} numRows
 * @return {number[][]}
 */
 var generate = function(numRows) {
    let ans=[[1]]
    for (i=0;i<numRows-1;i++){
        let temp=[0].concat(ans[ans.length-1],[0])
        let row=[]
        for(j=0;j<ans[ans.length-1].length+1;j++){
            row.push(temp[j]+temp[j+1])
        }
        ans.push(row)
    }
    return (ans)
};