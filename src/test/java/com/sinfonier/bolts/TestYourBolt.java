package com.sinfonier.bolts;


import com.sinfonier.utils.ComponentType;
import com.sinfonier.utils.Runner;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.util.Map;

public class TestYourBolt {

    @Before
    public void setUp() {
    }


    @Test
    public void testYourBolt() {
        // Instantiate your module

    	// Java
        //Map<String, Object> result = Runner.run(ComponentType.BOLT, YourBolt.class);

    	// Python
    	//Map<String, Object> result = Runner.runPy(ComponentType.BOLT, LauncherPyBolts.class, "pythonboltfile.py");
        Map<String, Object> result = Runner.runPy(ComponentType.BOLT, LauncherPyBolts.class, "addtimestamp.py");

        // Code the test conditions
        /*Assert.assertNotNull(result.get("username"));
        Assert.assertEquals("asdfasdf", result.get("username").toString());

        Assert.assertNotNull(result.get("join_date"));
        Assert.assertEquals("1217775487", result.get("join_date").toString());*/
    }
}
