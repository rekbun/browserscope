/**
 * @fileoverview 
 * Common constants and variables used in the RTE test suite.
 *
 * TODO: license! $$$
 *
 * @version 0.1
 * @author rolandsteiner@google.com
 */

// Constant for indicating a test setup is unsupported or incorrect
// (threw exception).
var SETUP_BAD_SELECTION_SPEC  = 'BAD SELECTION SPECIFICATION IN TEST OR EXPECTATION STRING';
var SETUP_HTML_EXCEPTION      = 'EXCEPTION WHEN SETTING TEST HTML';
var SETUP_SELECTION_EXCEPTION = 'EXCEPTION WHEN SETTING SELECTION';

// Constants for indicating a test action is unsupported (threw exception).
var UNSUPPORTED_COMMAND_EXCEPTION = 'UNSUPPORTED COMMAND';
var VERIFICATION_EXCEPTION        = 'EXCEPTION DURING TEST VERIFICATION';

// Constants for indicating an exception in score handling.
var SCORE_EXCEPTION = 'EXCEPTION WHEN WRITING TEST SCORES';

// Selection comparison result contants.
var RESULT_SETUP_EXCEPTION        = 0;
var RESULT_EXECUTION_EXCEPTION    = 1;
var RESULT_VERIFICATION_EXCEPTION = 2;
var RESULT_HTML_DIFFS             = 3;
var RESULT_SELECTION_DIFFS        = 4;
var RESULT_EQUAL                  = 5;

// Special attributes used to mark selections within elements that otherwise
// have no children. Important: attribute name MUST be lower case!
var ATTRNAME_SEL_START = 'bsselstart';
var ATTRNAME_SEL_END   = 'bsselend';

// DOM node type constants.
var DOM_NODE_TYPE_ELEMENT = 1;
var DOM_NODE_TYPE_TEXT    = 3;
var DOM_NODE_TYPE_COMMENT = 8;

// Test parameter names
var PARAM_DESCRIPTION      = 'desc';
var PARAM_PAD              = 'pad';
var PARAM_COMMAND          = 'command';
var PARAM_VALUE            = 'value';
var PARAM_EXPECTED         = 'expected';
var PARAM_CHECK_ATTRIBUTES = 'checkAttrs';
var PARAM_CHECK_STYLE      = 'checkStyle';
var PARAM_CHECK_CLASS      = 'checkClass';
var PARAM_CHECK_ID         = 'checkID';
var PARAM_CHECK_SELECTION  = 'checkSel';
var PARAM_STYLE_WITH_CSS   = 'styleWithCSS';
var PARAM_ALLOW_EXCEPTION  = 'allowException';

// DOM elements used for the tests.
var editorElem = null;
var editorWin  = null;
var editorDoc  = null;
var contentEditableElem = null;

// Variables holding the current suite and test for simplicity.
var currentSuite           = null;  // object specifiying the current test suite
var currentSuiteScoreID    = '';    // ID of the element showing the final scores for the suite
var currentClass           = null;  // sub-object of currentSuite, specifying the current class
var currentClassID         = '';    // ID string of the current class - one of testClasses, below
var currentClassScoreID    = '';    // ID of the element showing the final scores for the class
var currentTest            = null;  // sub-object of currentClass, specifying the current test
var currentTestID          = '';    // ID string of the current test within the class
var currentID              = '';    // totally unique ID, concatenated '<suite ID>-<test ID>'
var currentResultHTML      = '';    // HTML string after executing the/all command(s)
var currentOutputTable     = null;  // HTML table for the current suite + class
var currentBackgroundShade = 'Lo';  // to facilitate alternating table row shading

// Classes of tests
var testClassIDs = ['Finalized', 'RFC', 'Proposed'];

// Dictionaries storing the numeric results.
var counts        = {};
var scoresStrict  = {};
var scoresPartial = {};

// Beacon results (seed, or the beacon will fail).
var beaconStrict  = ['selection=0', 'apply=0', 'applyCSS=0', 'change=0', 'changeCSS=0', 'unapply=0', 'unapplyCSS=0', 'delete=0', 'forwarddelete=0', 'insert=0'];
var beaconPartial = ['selection=0', 'apply=0', 'applyCSS=0', 'change=0', 'changeCSS=0', 'unapply=0', 'unapplyCSS=0', 'delete=0', 'forwarddelete=0', 'insert=0'];