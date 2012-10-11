package
{
    import flash.display.Sprite;
    import flash.net.URLLoader;
    import flash.net.URLRequest;
    import flash.events.Event;
    
    public class LoadXML extends Sprite
    {
        private var quiz:XML;
        public function Chapter11()
        {
            var loader:URLLoader = new URLLoader(new URLRequest("quiz.xml"));
            loader.addEventListener(Event.COMPLETE, onXMLLoad, false,0,true);
        }
        
        private function onXMLLoad(e:Event):void {
            quiz = XML(e.target.data);
            trace(quiz.problem[0].question); // trace "What does this book cover?"
        }
    }
}
