function filter_JSON() {
            var max_sentiment = document.forms["myForm"]["max_sentiment"].value;
            var min_sentiment = document.forms["myForm"]["min_sentiment"].value;
            var max_count = document.forms["myForm"]["max_count"].value;
            var min_count = document.forms["myForm"]["min_count"].value;

            if (max_sentiment == "")
                max_sentiment = 1 ;
            if (min_sentiment == "")
                min_sentiment = -1 ;
            if (max_count == "")
                max_count = 10000;
            if (min_count == "")
                min_count = 0 ;

            jsonObj = jsonObj_main;
            var jsonObj_temp=[];
            i = 0;k = 0;
            while (i < jsonObj.length)
            {
                if (jsonObj[i].count >= min_count && jsonObj[i].count <= max_count && jsonObj[i].sentiment >= min_sentiment && jsonObj[i].sentiment <= max_sentiment )
                { jsonObj_temp[k] = jsonObj[i];k++; }
                i++;
            }

            jsonObj = jsonObj_temp;
            displayJSON(jsonObj);
            
        }