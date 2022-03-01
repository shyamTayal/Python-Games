class Solution {
private:
    map<string, int> logger;
    vector<string> storage;
    
    vector<int> prisoncell(string str, int n){
        int i, val = 0, end=0,flag =-1; // not found repetition
        
        for(i=1;i<=n;++i){
            string temp(8,'0');
            
            // create next iteration
            for(int j=1;j<7;++j){
                if(str[j-1] == str[j+1])
                    temp[j] = '1';
            }
            // transfer for next iteration
            str = temp;
            // if find  temp in map then take the start=val, end=i and flag=found repetition
            if(logger.find(temp) != logger.end()){
                val=logger[temp];
                flag = 1;
                end = i;
                break;             // breaking after full execution of block
            }
            // push in the map and vector
            logger[str] = end;
            storage.push_back(str);
        }
        return {val,end, flag};
    }
public:
    vector<int> prisonAfterNDays(vector<int>& cells, int n) {
        string str;
        for(auto e : cells){
            str.push_back((char)(e+'0'));
        }
        // push initial string
        storage.push_back(str);
        logger[str] = 0;
        // call helper function
        vector<int> vec = prisoncell(str, n);
        
        // debugging
        cout<<vec[0]<<' '<<vec[1]<<' '<<vec[2]<<'\n';
        string ans;
        if(vec[2] == -1){
            ans = storage.back();
        }
        // index = remainder of (total left)/(end - start +1) + start 
        else{
            int index = (n-vec[0])%(vec[1]-vec[0]) + vec[0] ; 
            cout<<index<<'\n';
            ans = storage[index];
           
        }
        // if found repetition then answer is reverse of the finding
        
        
        vector<int> res;
        for(auto ch : ans)
            res.push_back((int)(ch-'0'));
        
        return res;
    }
};
